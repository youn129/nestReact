import { Module } from '@nestjs/common';
import { AuctionController } from './auction.controller';
import { EbayTokenService } from '../ebay-token.service';

@Module({
  controllers: [AuctionController],
  providers: [EbayTokenService],
})
export class AuctionModule {}
