import { ConflictException, Injectable } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { UsersService } from '../users/users.service';
import * as bcrypt from 'bcrypt';

@Injectable()
export class AuthService {
  constructor(
    private readonly usersService: UsersService,
    private readonly jwtService: JwtService,
  ) {}

  async signUp(username: string, email: string, password: string) {
    const existingUser = await this.usersService.findUserByUsername(username);
    if (existingUser) {
      throw new ConflictException('Username is already taken.');
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const user = await this.usersService.createUser(
      username,
      hashedPassword,
      email,
    );
    return user;
  }
}
