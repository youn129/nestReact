import { Controller, Get, Query } from '@nestjs/common';
import { AppService } from './app.service';
import { exec } from 'child_process';
import { promisify } from 'util';
import { EbayTokenService } from './ebay-token.service';
import axios from 'axios';

const execAsync = promisify(exec);

@Controller('api')
export class AppController {
  constructor(
    private readonly appService: AppService,
    private readonly ebayTokenService: EbayTokenService,
  ) {}

  @Get('data')
  getHealthStatus() {
    return this.appService.getHealthStatus();
  }

  @Get('get-ebay-token')
  async getEbayAccessToken() {
    try {
      const token = await this.ebayTokenService.getAccessToken();
      return { accessToken: token };
    } catch (error) {
      console.error('Error generating eBay access token:', error.message);
      return { error: 'Failed to get access token' };
    }
  }

  @Get('auctions')
  async getAuctionItems() {
    try {
      const auctionItems = [
        {
          id: 1,
          title: 'Item A',
          currentBid: 100,
          endTime: '2024-12-30T12:00:00Z',
        },
        {
          id: 2,
          title: 'Item B',
          currentBid: 200,
          endTime: '2024-12-31T14:00:00Z',
        },
      ];
      return { data: auctionItems };
    } catch (error) {
      console.error('Error fetching auctions:', error.message);
      return { error: error.message };
    }
  }

  @Get('fetch-auctions')
  async fetchAuctionData(
    @Query('query') query: string = 'laptop',
    @Query('popular') popular?: string,
  ) {
    try {
      const accessToken = await this.ebayTokenService.getAccessToken();
      console.log('Access Token:', accessToken);

      const headers = {
        Authorization: `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
      };

      const url = `https://api.ebay.com/buy/browse/v1/item_summary/search?q=${query}&filter=buyingOptions:{AUCTION}${
        popular === 'true' ? '&sort=popularityRank' : ''
      }`;

      console.log('eBay API URL:', url);

      const response = await axios.get(url, { headers });

      console.log('eBay API Response:', response.data);

      if (response.data && response.data.itemSummaries) {
        return { data: response.data.itemSummaries };
      } else {
        console.warn('No itemSummaries in response:', response.data);
        return { data: [] };
      }
    } catch (error) {
      console.error('Error fetching auction data:', error.message);
      return { error: 'Failed to fetch auction data. Please try again later.' };
    }
  }

  @Get('coin-data')
  async getCoinData() {
    try {
      const command = 'python dist/python/coin.py';
      console.log(`Executing command: ${command}`);

      const { stdout, stderr } = await execAsync(command);

      if (stderr) {
        console.warn('Python script stderr (ignored):', stderr.trim());
      }

      console.log('Python script stdout:', stdout);

      const parsed = JSON.parse(stdout.trim());
      console.log('Parsed Python output:', parsed);

      return { data: parsed };
    } catch (error) {
      console.error('Error in getCoinData:', error.message);
      return { error: error.message };
    }
  }
}
