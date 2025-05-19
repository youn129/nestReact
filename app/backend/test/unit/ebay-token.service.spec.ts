import { Test, TestingModule } from '@nestjs/testing';
import { EbayTokenService } from '../../src/ebay-token.service';
import { ConfigService } from '@nestjs/config';
import axios from 'axios';

jest.mock('axios');
const mockedAxios = axios as jest.Mocked<typeof axios>;

describe('EbayTokenService', () => {
  let service: EbayTokenService;
  let configService: ConfigService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [
        EbayTokenService,
        {
          provide: ConfigService,
          useValue: {
            get: (key: string) => {
              const env = {
                EBAY_CLIENT_ID: 'test-client-id',
                EBAY_CLIENT_SECRET: 'test-secret',
                EBAY_REFRESH_TOKEN: 'test-refresh-token',
              };
              return env[key];
            },
          },
        },
      ],
    }).compile();

    service = module.get<EbayTokenService>(EbayTokenService);
    configService = module.get<ConfigService>(ConfigService);
  });

  it('should refresh and return access token if token is expired', async () => {
    const mockToken = 'mocked-access-token';
    const mockExpiresIn = 3600;

    mockedAxios.post.mockResolvedValue({
      data: {
        access_token: mockToken,
        expires_in: mockExpiresIn,
      },
    });

    const token = await service.getAccessToken();

    expect(mockedAxios.post).toHaveBeenCalled();
    expect(token).toBe(mockToken);
  });

  it('should return existing token if it is still valid', async () => {
    service['accessToken'] = 'valid-token';
    service['tokenExpiry'] = Math.floor(Date.now() / 1000) + 600;

    mockedAxios.post.mockClear();
    const token = await service.getAccessToken();

    expect(mockedAxios.post).not.toHaveBeenCalled();
    expect(token).toBe('valid-token');
  });

  it('should throw error if axios fails', async () => {
    mockedAxios.post.mockRejectedValue(new Error('Request failed'));

    service['accessToken'] = null;
    service['tokenExpiry'] = null;

    await expect(service.getAccessToken()).rejects.toThrow(
      'Token refresh failed',
    );
  });
});
