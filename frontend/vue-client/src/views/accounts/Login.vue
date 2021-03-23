<template>
  <div>
    <div class="main">
      <h1 class="main-title">Log In</h1>
    </div>
    <div class="login-form">
      <div>
        <label for="username">아이디 </label>
        <input placeholder="아이디를 입력해주세요" type="text" id="username" v-model="credentials.username">
      </div>
      <div class="password-input">
        <label for="password">비밀번호 </label>
        <input placeholder="비밀번호를 입력해주세요" type="password" id="password" v-model="credentials.password" @keypress.enter="login(credentials)">
      </div>
      <b-button variant="primary" @click="login(credentials)">로그인</b-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data() {
    return {
      credentials: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    login({ username, password }) {
      axios.post('http://127.0.0.1:8000/accounts/api-token-auth/', { username, password })
        .then(res => {
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$fire({
              title: "로그인 성공!",
              text: "안녕하세요!🤩 MOVIEEKER입니다!",
              type: "success",
              timer: 3000
            }).then(r => {
            console.log(r.value);
            });
          this.$router.push({ name: 'Home' })
        })
    }
  }
}
</script>

<style scoped>
  .main {
    height: 400px;
    background-image: url(https://cdn.wadiz.kr/ft/images/green001/2019/1114/20191114141744658_46316.gif);
    margin-bottom: 80px;
    background-size: 1920px;
    filter: grayscale(100%);
  }

  .main-title {
    color:white;
    position: relative;
    padding-top: 180px;
    font-weight: bold;
  }

  .login-form {
    margin-bottom: 80px;
  }

  .password-input {
    margin-bottom: 20px;
  }

  label {
    font-weight: bold;
    color: rgb(41, 109, 236);
    margin-right: 5px;
  }

  input {
    width: 250px;
  }

</style>