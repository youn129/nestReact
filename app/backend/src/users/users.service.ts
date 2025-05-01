import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { User } from './schemas/user.schema';

@Injectable()
export class UsersService {
  constructor(
    @InjectModel(User.name) private readonly userModel: Model<User>,
  ) {}

  // 유저 등록
  async createUser(username: string, password: string, email: string) {
    const newUser = new this.userModel({ username, password, email });
    return newUser.save();
  }

  // 유저 조회
  async findUserByUsername(username: string): Promise<User | null> {
    return this.userModel.findOne({ username }).exec();
  }

  // 찜 목록에 상품 추가
  async addFavorite(userId: string, itemId: string): Promise<User | null> {
    return this.userModel
      .findByIdAndUpdate(
        userId,
        { $addToSet: { favorites: itemId } },
        { new: true },
      )
      .exec();
  }

  // 찜 목록 조회
  async getFavorites(userId: string): Promise<string[]> {
    const user = await this.userModel.findById(userId).exec();
    return user ? user.favorites : [];
  }
}
