import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import axios from 'axios';

@Injectable()
export class EbayTokenService {
  private accessToken: string | null = null;
  private refreshToken: string;
  private clientId: string;
  private clientSecret: string;
  private tokenExpiry: number | null = null;
  private authUrl = 'https://api.ebay.com/identity/v1/oauth2/token';

  constructor(private readonly configService: ConfigService) {
    // 환경 변수에서 값 불러오기
    this.clientId = this.configService.get<string>('EBAY_CLIENT_ID', '');
    this.clientSecret = this.configService.get<string>(
      'EBAY_CLIENT_SECRET',
      '',
    );
    this.refreshToken = this.configService.get<string>(
      'EBAY_REFRESH_TOKEN',
      '',
    );
  }

  async refreshAccessToken() {
    try {
      const auth = Buffer.from(
        `${this.clientId}:${this.clientSecret}`,
      ).toString('base64');
      const headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        Authorization: `Basic ${auth}`,
      };
      const body = new URLSearchParams({
        grant_type: 'refresh_token',
        refresh_token: this.refreshToken,
        scope: 'https://api.ebay.com/oauth/api_scope',
      });

      const response = await axios.post(this.authUrl, body.toString(), {
        headers,
      });
      const data = response.data;

      this.accessToken = data.access_token;
      this.tokenExpiry = Math.floor(Date.now() / 1000) + data.expires_in;

      console.log('Access token refreshed:', this.accessToken);
    } catch (error) {
      console.error('Failed to refresh access token:', error.message);
      throw new Error('Token refresh failed');
    }
  }

  async getAccessToken(): Promise<string> {
    if (
      !this.accessToken ||
      !this.tokenExpiry ||
      Date.now() / 1000 > this.tokenExpiry - 60
    ) {
      await this.refreshAccessToken();
    }
    return this.accessToken;
  }
}
