import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { Document } from 'mongoose';

export type UserDocument = User & Document;

@Schema()
export class User extends Document {
  @Prop({ required: true, unique: true })
  username: string;

  @Prop({ required: true })
  password: string;

  @Prop({ default: [] })
  favorites: string[]; // 사용자가 찜한 상품 ID 목록
}

export const UserSchema = SchemaFactory.createForClass(User);
