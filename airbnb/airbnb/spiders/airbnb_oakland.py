# -*- coding: utf-8 -*-
import scrapy
import json

from airbnb.items import AirbnbItem

class AirbnbOaklandSpider(scrapy.Spider):
    name = 'airbnb_oakland'
    allowed_domains = ['www.airbnb.com']

    def __init__(self, search_term='Downtown Oakland CA', *args, **kwargs):
        super(AirbnbOaklandSpider, self).__init__(*args, **kwargs)
        self.search_term = search_term


    def start_requests(self):
        url = ('https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&'
               'auto_ib=false&client_session_id=cdf3e269-6f40-441f-8d3d-97cd21933c7e&'
               'currency=USD&current_tab_id=home_tab&experiences_per_grid=20&fetch_filters=true&'
               'guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&'
               'is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&'
               'items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en&metadata_only=false&'
               'place_id=ChIJg3mNR7KAj4AR6MAZAwOAIlM&'
               'query={0}&'
               'query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&s_tag=HaxHO0ml&'
               'satori_version=1.2.0&screen_height=794&screen_size=small&screen_width=742&'
               'search_type=pagination&selected_tab_id=home_tab&show_groupings=true&'
               'supports_for_you_v3=true&timezone_offset=-480&version=1.7.3')
        url = url.format(self.search_term)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        listing_data = data.get('explore_tabs')[0].get('sections')[0].get('listings')
        country = str(data.get('metadata').get('geography').get('country'))

        for listing in listing_data:
            listing_item = AirbnbItem()
            details = listing.get('listing')
            price = listing.get('pricing_quote')
            
            listing_id = str(details.get('id'))
            rate = price.get('rate').get('amount')
            rate_w_service = price.get('rate_with_service_fee').get('amount')

            listing_item['listing_id'] = listing_id
            listing_item['title'] = str(details.get('name'))
            listing_item['country'] = country
            listing_item['city'] = str(details.get('localized_city'))
            listing_item['lat'] = details.get('lat')
            listing_item['lon'] = details.get('lon')
            listing_item['bedrooms'] = details.get('bedrooms')
            listing_item['bathrooms'] = details.get('bathrooms')
            listing_item['max_occupancy'] = details.get('person_capacity')
            listing_item['service_fee'] = rate_w_service - rate

            yield listing_item