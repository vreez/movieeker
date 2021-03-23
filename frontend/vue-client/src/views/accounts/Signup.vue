<template>
  <div>
    <div class="main">
      <h1 class="main-title">Sign-Up</h1>
    </div>
    <div class="signup-form">
      <div>
        <label for="username">아이디</label>
        <input placeholder="어떤 아이디가 좋을까요?" type="text" id="username" v-model="credentials.username">
      </div>
      <div>
        <label for="password">비밀번호</label>
        <input placeholder="비밀번호 입력해주세요!" type="password" id="password" v-model="credentials.password">
      </div>
      <div class="confirm">
        <label for="passwordConfirmation">비밀번호 확인</label>
        <input placeholder="비밀번호를 다시한번 입력해주세요!" type="password" id="passwordConfirmation" 
          v-model="credentials.passwordConfirmation" 
          @keypress.enter="signup(credentials)">
      </div>
      <b-button variant="primary" @click="signup(credentials)">회원가입</b-button>
    </div>
  </div>  
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup({ username, password, passwordConfirmation }) {
      const userData = {
        username,
        password,
        passwordConfirmation,
      }

      if (password === passwordConfirmation) {
        axios.post('http://127.0.0.1:8000/accounts/signup/', userData)
          .then(() => {
            // 회원가입 정상 진행 (server)
            this.$fire({
              title: "회원가입 성공!",
              text: "와! MOVIEEKER의 회원이 되신 것을 환영합니다!🎉🎉",
              type: "success",
              timer: 3000
            }).then(r => {
            console.log(r.value);
            });
            this.$router.push({ name: 'Login' })
          })
      } else {
        alert('작성된 비밀번호가 다릅니다.')
      }
      
    }
  }
}
</script>

<style scoped>
  .main {
    height: 400px;
    background-image: url(https://cdn.lowgif.com/small/c779994a73ec6284-bottom-gif-find-share-on-giphy.gif);
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

  .signup-form {
    margin-bottom: 80px;
  }

  .confirm {
    margin-bottom: 20px;
  }

  label {
    font-weight: bold;
    color: rgb(41, 109, 236);
    margin-right: 5px;
  }

  input {
    width: 300px;
  }
</style>