import { Controller, Post, Body, BadRequestException } from '@nestjs/common';
import { AuthService } from './auth.service';

@Controller('auth')
export class AuthController {
  constructor(private readonly authService: AuthService) {}

  @Post('signup')
  async signUp(
    @Body('username') username: string,
    @Body('email') email: string,
    @Body('password') password: string,
  ) {
    // 유효성 검사
    if (!username || !email || !password) {
      throw new BadRequestException('All fields are required.');
    }

    const user = await this.authService.signUp(username, email, password);
    return { message: 'User registered successfully', user };
  }
}
