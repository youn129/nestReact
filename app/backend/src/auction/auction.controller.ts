import { Controller, Get, Query } from '@nestjs/common';
import { EbayTokenService } from '../ebay-token.service';
import axios from 'axios';

@Controller('auctions')
export class AuctionController {
  constructor(private readonly ebayTokenService: EbayTokenService) {}

  // eBay API를 통해 외부 경매 데이터 가져오기
  @Get('fetch-auctions')
  async fetchAuctions(
    @Query('query') query: string,
    @Query('popular') popular: string,
  ) {
    console.log('Controller fetch-auctions called');
    const isPopular = popular === 'true';

    try {
      const accessToken = await this.ebayTokenService.getAccessToken();

      const url = `https://api.ebay.com/buy/browse/v1/item_summary/search?q=${encodeURIComponent(query)}&filter=buyingOptions:{AUCTION}${
        isPopular ? '&sort=popularityRank' : ''
      }`;

      const response = await axios.get(url, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
      });

      console.log(
        `Fetched ${response.data.itemSummaries?.length || 0} auctions`,
      );
      return { data: response.data.itemSummaries || [] };
    } catch (error) {
      console.error('🚨 Error in fetch-auctions Controller:', error.message);
      throw new Error('Failed to fetch auction data');
    }
  }
}
