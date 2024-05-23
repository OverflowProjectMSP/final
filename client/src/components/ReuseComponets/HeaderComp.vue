<script>
import axios from 'axios';

// import BlindWindow from '../СomponetsForPages/BlindWindow.vue'

export default {

  components: {
    // BlindWindow,
  },

  data() {
    return {
      Errors: [{
        title: `Функция в разработке.`,

      }],
      ShowLogin: true,
      avatar: 'src/assets/Header/AvatarDef.svg',
      id: ''
    }

  },
  methods: {
    Open() {
      this.Show = !this.Show;
    },
    LoginPage() {
      this.$router.push('/Login');
    },
    async loadAvatar() {
      let res = await axios.get('/avatar');
      this.avatar = res.data.link;
      if (this.avatar == "No") {
        this.avatar = "src/assets/Header/AvatarDef.svg";
      } else {
        this.avatar = this.avatar;
      }
    },
    async loadLogin() {
      setTimeout(()=>{console.log(1)}, 3000 )
      let res = await axios.get(`/check-r`);
      this.ShowLogin = res.data.all;
      console.log(this.ShowLogin)
      if (this.ShowLogin == "true") {
        this.ShowLogin = false;
        
        this.getId()
      } else if (this.ShowLogin == "false") {
        this.ShowLogin = true;
      }
    },
    async getId(){
      let res = await axios.get(`/session`);
      this.id = res.data.id
      console.log(this.id)
    }
  },
  mounted() {
    this.loadLogin();
    this.loadAvatar()
  }
}

</script>
<template>


  <header id="1">
    <nav class="navbar navbar-expand-xl  d-flex align-items-center rounded-0">
      <div class="container-fluid ">
        <a class="navbar-brand" href="/">
          <div class="logo-container mt-1"><img src="../../assets/Header/Logo.png" alt="" class="logo"></div>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div class="container-contant"></div>
          <h4 class="nav-item mr-0 ml-0">
            <a class="nav-link mt-2 head" aria-current="page" href="/">UpFollow</a>
          </h4>
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 mb-2">
            <li class="nav-item mt-1" style="cursor: pointer;">
              <a class="nav-link text-white" href="/Quetions">Вопросы</a>
            </li>
            <li class="nav-item dropdown mt-1">
              <a class="nav-link  text-white" href="/States">
                Статьи
              </a>

            </li>
            <li class="nav-item mt-1" style="cursor: pointer;">
              <a class="nav-link text-white" aria-disabled="true" href="/ForumPage">Форум</a>
            </li>
          </ul>
          <div class="container-form">

          </div>
          <!-- <form class="d-flex form" role="search">
            <input class="form-control  inp " type="search" placeholder="Найти статью" aria-label="Search">

          </form> -->
          <div class="them-container" v-if="this.ShowLogin">
            <button type="button" class=" btn-login" @click="LoginPage">Войти</button>
          </div>
          <div class="ava-container" v-else>
            <a :href="`/Profile?id=${this.id}`"> <img
                :src="avatar"
                alt="" class="ava"></a>
          </div>
        </div>
      </div>
    </nav>
  </header>

</template>
<style scoped>
.btn-login{
  background: rgb(255, 255, 255);
  border: none;
  height: 45px;
  width: 100px;
  border-radius: 10px;
}
.head{
  margin-left: 30px;
  font-weight: 700;
  font-size: 30px;

}
.icon-btn {
  margin-top: -20px;
}

header {
  background-color: #3B82F6;
  width: auto;
  border-radius: 0px 0px 0px 0px;
}


.ava {
  width: 52px;
  height: 49px;
  margin-right: 2px;
  margin-left: 5px;
  border-radius: 10px;
  cursor: pointer;
}

.form {
  margin-right: 20px;

}

.form input {
  width: 350px;
}

.them {
  width: 35px;
  height: 35px;
  margin-right: 10px;
  margin-left: 3px;
  cursor: pointer;

}

.button-search {
  background-color: white;
  color: black;
}



header {
  width: auto !important;

}



.logo {
  width: 80px;
  height: 50px;
  margin-right: -15px;
  margin-left: 0px;
  align-items: center;
}

.container-form {
  margin-top: 0px;
  margin-bottom: 10px;
}

.navbar-nav {
  display: flex;
  gap: 50px;
  margin-left: max(5vw, 60px);
  margin-bottom: 1px;
}

.collapse {
  margin-top: 0px;
}

.collapse h4 {

  margin-top: 5.5px;
  margin-right: 10px;
  margin-left: 0px;
  font-weight: 400;
}

.nav-item {
  color: white;
}

li {
  font-size: 20px;
  font-weight: 500;
}

.navbar {
  height: 1%;
  border-radius: 10px;
  display: flex;
}

.inp {
  width: 440px;
  border-radius: 9px;
}

.nav-link {
  color: white;
}



.btn-login{
  transition: all, 0.4s;
}

.navbar-toggler-icon {
  border-radius: 10px;
  width: 50px;
  height: 50px;
}


@media (hover: hover) {
  .btn-login:hover{
    background-color: #000000;
    color: white;
  }

  .nav-link:hover {
    color: rgb(255, 255, 255);
  }

  .button-search:hover {
    background-color: rgb(255, 255, 255);
    color: white;
    transition: all 1s;
  }
}

@media (max-width: 1200px) {

  .navbar-nav {
    gap: 0px;
    margin-left: 14px;
  }

  .ava {
    margin-top: -70px;
    margin-left: 110px;
  }
.head{
  margin-left: 10px;
}

}

@media (max-width: 1000px) {

  .navbar-nav {
    gap: 0px;
    margin-left: 14px;
  }

  .ava {
    margin-top: -70px;
  }

  .them {
    margin-left: 9%;
    margin-top: 5%;
  }

  .form input {
    width: 210px;
  }

}

@media (max-width: 800px) {

  .them {
    margin-left: 10%;
    margin-top: 5%;
  }
}

@media (max-width: 600px) {

  .them {
    margin-left: 17%;
    margin-top: 5%;
  }
}

@media (max-width: 420px) {

  .them {
    margin-left: 20%;
    margin-top: 5%;
  }
}

@media (max-width: 340px) {

  .them {
    margin-left: 25%;
    margin-top: 5%;
  }
}
</style>