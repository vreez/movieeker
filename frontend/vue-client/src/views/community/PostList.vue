<template>
  <div>
    <div class=main>
      <h1 class="main-title">
        자유게시판
      </h1>
    </div>
    <div class="listWrap">
			<table class="table">
				<tr class="tableTitle">
					<th>No.</th>
					<th class="title">제목</th>
					<th>아이디</th>
					<th>날짜</th>
				</tr>
				<tr v-for="(post, idx) in posts" :key="idx">
					<td>{{ post.id }}</td>
					<td class="txt_left"><a href="javascript:;" @click="goToDetail(post)">{{post.title}}</a></td>
					<td>{{ post.user }}</td>
					<td>{{ post.updated_at | moment('YYYY-MM-DD')}}</td>
				</tr>
			</table>
		</div>
    <b-button class="button" variant="outline-primary"><a href="javascript:;" @click="goToWrite" class="btn">글 작성하기</a></b-button>
  </div>  
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import vueMoment from 'vue-moment'
Vue.use(vueMoment)

export default {
  name: 'PostList',

  data: function () {
    return {
      posts: [],
      
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    goToWrite(){ //게시글 확인 페이지로 이동
			this.$router.push({path:'/community/create',query:this.body});
    },
    goToDetail(post) {
      this.$router.push({path:`/community/${post.id}`, query:post})
    
    },
    getPosts: function () {
      const config = this.setToken()

      axios.get('http://127.0.0.1:8000/community/', config)
        .then((res) => {
          console.log('list get요청')
          console.log(res)
          console.log(res.data)
          this.posts = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deletePost: function (post) {
      const config = this.setToken()

      axios.delete(`http://127.0.0.1:8000/community/${post.id}/`, config)
        .then((res) => {
          console.log(res)
          const targetPostIdx = this.posts.findIndex((post) => {
            return post.id === res.data.id
          })
          this.posts.splice(targetPostIdx, 1)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updatePostStatus: function (post) {
      const config = this.setToken()

      const postItem = {
        ...post,
        completed: !post.completed
      }

      axios.put(`http://127.0.0.1:8000/community/${post.id}/`, postItem, config)
        .then((res) => {
          console.log('수정@@@')
          console.log(res)
          post.completed = !post.completed
        })
      },
    },
 
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getPosts()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}

</script>

<style scoped>

  .line {
    width: 60%;
    margin-bottom: 25px;
  }

  .post-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }

  ul {
    list-style: none;
  }

  colgroup {
    width: 60%;
  }

  .listWrap {
    margin-bottom: 30px;
  }

  .title {
    width: 300px;
  }

  .tableTitle {
    margin-bottom: 30px;
  }

  .main {
    height: 400px;
    background-image: url(https://media2.giphy.com/media/xUA7b3v67J4zaqi6GI/source.gif);
    margin-bottom: 20px;
    background-size: 1920px;
    filter: grayscale(100%);
  }

  .main-title {
    color:white;
    position: relative;
    padding-top: 180px;
    font-weight: bold;
  }

  .button {
    margin-bottom: 150px;
  }

</style>