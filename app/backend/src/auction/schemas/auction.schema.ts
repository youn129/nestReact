import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { Document } from 'mongoose';

@Schema()
export class Auction extends Document {
  @Prop({ required: true })
  title: string;

  @Prop({ required: true })
  currentBid: number;

  @Prop({ required: true })
  endTime: Date;
}

export const AuctionSchema = SchemaFactory.createForClass(Auction);
