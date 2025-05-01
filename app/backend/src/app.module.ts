import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { join } from 'path';
import { EbayTokenService } from './ebay-token.service';
import { AuctionModule } from './auction/auction.module';
import { UsersModule } from './users/users.module';
import { AuthModule } from './auth/auth.module';

@Module({
  imports: [
    // ConfigModule 설정
    ConfigModule.forRoot({
      envFilePath: join(__dirname, '..', '..', '.env'),
      isGlobal: true, // ConfigModule을 전역 모듈로 설정
    }),

    // MongooseModule 설정
    MongooseModule.forRootAsync({
      imports: [ConfigModule],
      useFactory: (configService: ConfigService) => {
        const mongoUri = configService.get<string>('MONGO_ATLAS_URI');
        console.log(`Connecting to MongoDB Atlas: ${mongoUri}`);
        return { uri: mongoUri };
      },
      inject: [ConfigService],
    }),

    // 모듈 추가
    AuctionModule,
    UsersModule,
    AuthModule,
  ],
  controllers: [AppController],
  providers: [AppService, EbayTokenService],
})
export class AppModule {}
