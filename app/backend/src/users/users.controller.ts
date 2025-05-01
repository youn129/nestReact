import { Controller, Post, Get, Body, Param } from '@nestjs/common';
import { UsersService } from './users.service';
import { User } from './schemas/user.schema';

@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  // 유저 등록
  @Post()
  async createUser(
    @Body('username') username: string,
    @Body('password') password: string,
    @Body('email') email: string,
  ): Promise<User> {
    return this.usersService.createUser(username, password, email);
  }

  // 유저 조회
  @Get(':username')
  async findUserByUsername(
    @Param('username') username: string,
  ): Promise<User | null> {
    return this.usersService.findUserByUsername(username);
  }

  // 찜 목록 추가
  @Post(':userId/favorites')
  async addFavorite(
    @Param('userId') userId: string,
    @Body('itemId') itemId: string,
  ): Promise<User | null> {
    return this.usersService.addFavorite(userId, itemId);
  }

  // 찜 목록 조회
  @Get(':userId/favorites')
  async getFavorites(@Param('userId') userId: string): Promise<string[]> {
    return this.usersService.getFavorites(userId);
  }
}
