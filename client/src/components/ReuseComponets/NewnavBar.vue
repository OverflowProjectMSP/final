<script>
import axios from 'axios';

export default {
  data() {
    return {
      burg: true,
      avatar: 'src/assets/Header/AvatarDef.svg',
      id: '',
    };
  },
  methods: {
    goto(name) {
      this.$router.push(name);
    },

    burgmenu() {
      this.burg = !this.burg;
      
      console.log(5);
    },

    Open() {
      this.Show = !this.Show;
    },
    LoginPage() {
      this.$router.push('/Login');
    },

    async getUserSession() {
      let res = await axios.get(`/get-curent-avatar`);

      if(res.data.all != null) {
        this.ShowLogin = false;
        this.id = res.data.all.id;

        if (this.avatar == "No") {
          this.avatar = "src/assets/Header/AvatarDef.svg";
        } else {
          this.avatar = res.data.all.avatar;
        }

      } else {
        this.ShowLogin = true;
      }
    },
  },

  mounted() {
    this.getUserSession();
  }
};
</script>

<template>
    <div class="navbar">
        <div class="items">
            <div class="icon-img">
                <a href="/"><img src="../../assets/Main/uflogo.svg" alt=""></a>
                <a href="/"><h2 class="title-logo">UpFollow</h2></a>
                <p>2.0</p>
            </div>
            <div class="lin">
              <a href="/Questions" @click="goto(`/Quetions`)">Вопросы</a>
              <a href="/States" @click="goto(`/States`)">Статьи</a>
              <a href="/leaders" @click="goto(`/leaders`)">Лидеры</a>
              <a href="https://t.me/lif0ltn" target="_blank">Новости IT</a>
            </div>
            <div class="lin-phone" :class="{ linPhoneHide: burg}">
              <div class="mainlin">
                <a href="/Questions" @click="goto(`/Quetions`)">Вопросы</a>
                <a href="/States" @click="goto(`/States`)">Статьи</a>
                <a href="/leaders" @click="goto(`/leaders`)">Лидеры</a>
              </div>
              <div class="otherlin">
                <a href="https://t.me/lif0ltn" target="_blank">Новости IT</a>
              </div>
            </div>
            
        </div>
        <div class="enter">           
            <img class="burgmenu" src="../../assets/Main/burgmenu.svg" alt="" @click="burgmenu">
            <button v-if='!this.id' @click="goto(`/Login`)"><span>Войти</span></button>
            <a v-if='this.avatar && this.id' :href="`/Profile/` + this.id"><img :src="this.avatar" alt="Аватар"></a>
        </div>
    </div>
</template>

<style>
.navbar {

  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 0 30px 0 30px;

  border-radius: 25px;
  width: 97%;
  min-height: 70px !important;

  background-color: #629bf7;
}


.items {
  display: flex;
  align-items: center;
  gap: 50px;
}

.items img {
  width: 50px;
  margin-bottom: 8px;
}

.lin {
  display: flex;
  gap: 40px;
}

.lin-phone {
  position: absolute;
  display: flex;
  justify-content: space-evenly;
  gap: 30px;
  padding: 15px 5px;
  
  width: 400px;
  border-radius: 12px;
  top: 80px;
  right: 10px;
  background-color: rgba(98,155,247,0.9);
}


.burgmenu {
  width: 40px !important;
  height: 25px !important;
  border-radius: 0 !important;
  cursor: pointer;
  margin: 0 20px 0 0 !important;
}

.mainlin {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.lin-phone a {
  display: grid;
  place-items: center;
  width: 150px;
  height: 30px !important;
  background-color: #3d72d3;
  font-size: 20px !important;
  transition: all 200ms;
  border-radius: 5px;
}


.mainlin a:hover {
  opacity: 0.8;
}

.items a {
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  transition: 200ms;
}

.items a:hover {
  opacity: 0.7;
}

.title-logo {
  margin: 0;
  color: #fff;
  font-size: 24px;
  font-weight: 600;
}

.icon-img {
  display: flex;
  align-items: center;
  gap: 15px;

  border-right: 2px solid #fff;

  padding-right: 50px;

  position: relative;

}

.icon-img p {
  position: absolute;
  top: 0;
  right: 13px;

  color: #fff;
  font-size: 18px;
  font-weight: 600;
}

.icon-img a:hover {
  opacity: 0.8 !important;
}

.enter button {
  width: 120px;
  border-radius: 5px;
  color: #fff;
  background-color: rgba(0, 0, 0, 0);
  line-height: 42px;
  padding: 0;
  border: 2px solid #fff;
  position: relative;
  font-weight: 500;
  transition: all 200ms;
}


.enter button:hover {
  background-color: #fff !important;
  color: #619bf7;
}

.enter button span {
  font-weight: 500;
}


/*
.enter button span {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}

.enter button:before,
.enter button:after {
  position: absolute;
  content: "";
  background-color: #fff;
  transition: all 300ms ease;
}

.enter button:before {
  right: 0;
  bottom: 0;
  height: 0%;
  width: 3px;
}

.enter button:after {
  right: 0;
  bottom: 0;
  width: 0%;
  height: 2px;
}

.enter button:hover {
  color: #fff;
  background-color: #3d72d3;
}

.enter button:hover:before {
  height: 100%;
}

.enter button:hover:after {
  width: 100%;
}

.enter button span:before,
.enter button span:after {
  position: absolute;
  content: "";
  background-color: #fff;
  transition: all 300ms ease;
}

.enter button span:before {
  left: 0;
  top: 0;
  height: 0%;
  width: 2px;
}

.enter button span:after {
  left: 0;
  top: 0;
  width: 0%;
  height: 2px;
}

.enter button:hover span:before {
  height: 100%;
}

.enter button:hover span:after {
  width: 100%;
}



*/

.enter img {
  width: 55px;
  height: 55px;
  object-fit: cover;
  border-radius: 15px;
  transition: 200ms;
}

.enter img:hover {
  filter: brightness(85%);
}

@media (max-width: 970px) {

  .items {
    gap: 30px;
  }

  .items a {
    font-size: 17px;
  }
}

@media (max-width: 900px) {
  .navbar {
    padding: 0 20px;
  }

  .items img {
    width: 40px;
  }

  .icon-img {
    padding-right: 40px;
  }

  .icon-img p {
    right: 7px;
    top: -7px;
  }

  h2 {
    font-size: 20px;
  }

  .items a {
    font-size: 15px;
  }

  .enter button {
    width: 100px;
    height: 40px;
  }

  .enter button span {
    font-size: 17px;
  }
}

@media (max-width: 760px) {
  .lin {
    gap: 20px;
  }
}

@media (min-width: 720px) {
  .lin-phone {
    display: none;
  }
  
  .burgmenu {
    display: none;
  }
}

@media (max-width: 720px) {
  .lin {
    display: none;
  }

  .linPhoneHide {
    display: none;
  }

  .icon-img p {
    font-size: 15px;
    top: -4px;
    right: 10px;
  }

  .header {
    top: 0 !important;
  }

  .navbar {
    min-height: 60px !important;
    width: 100%;
    border-radius: 0 0 15px 15px !important;
  }

  .enter button {
    width: 100px !important;
    height: 30px;
    line-height: 30px;
  }

  .enter img {
    width: 48px;
    height: 48px;
  }

  .items img {
    width: 35px;
  }

  h2 {
    font-size: 16px !important;
  }

  
}

@media (max-width: 480px) {
  .lin-phone {
    width: 350px;
  }

  .enter button {
    width: 70px !important;
  }

  .enter span {
    font-size: 12px !important;
  }
}

@media (max-width: 395px) {
  .lin-phone {
    width: 310px;
  }

  .lin-phone {
    gap: 5px;
  }

  .lin-phone a {
    font-size: 16px !important;
    width: 130px;
  }
}
</style>
