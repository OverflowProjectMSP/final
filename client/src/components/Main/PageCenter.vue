<script>
import axios from 'axios';

export default {
  data() {
    return {
      langueges: ['TS', 'PHP', 'Python', 'JS', 'C#', 'Ruby', 'C++', 'Go', 'Java', 'Kotlin'],
      stylesLang: ['ts', 'php', 'py', 'js', 'cs', 'ruby', 'cpp', 'go', 'ja', 'ko'],
      links: ['ts', 'php', 'python', 'javascript', 'cs', 'ruby', 'cpp', 'go', 'java', 'kotlin'],
      index: 0,
      index1: 1,
      index2: 2,
      index3: 3,
      index4: 4,
      index5: 5,
      usersReg: 10
    }
  },
  methods: {
    nextLang() {
      this.index++;
      this.index1++;
      this.index2++;
      this.index3++;
      this.index4++;
      this.index5++;
      if (this.index == this.langueges.length) {
        this.index = 0;
      } else if (this.index1 == this.langueges.length) {
        this.index1 = 0;
      } else if (this.index2 == this.langueges.length) {
        this.index2 = 0;
      } else if (this.index3 == this.langueges.length) {
        this.index3 = 0;
      } else if (this.index4 == this.langueges.length) {
        this.index4 = 0;
      } else if (this.index5 == this.langueges.length) {
        this.index5 = 0;
      }
    },
    prevLang() {
      this.index--;
      this.index1--;
      this.index2--;
      this.index3--;
      this.index4--;
      this.index5--;
      if (this.index < 0) {
        this.index = this.langueges.length - 1;
      } else if (this.index1 < 0) {
        this.index1 = this.langueges.length - 1;
      } else if (this.index2 < 0) {
        this.index2 = this.langueges.length - 1;
      } else if (this.index3 < 0) {
        this.index3 = this.langueges.length - 1;
      } else if (this.index4 < 0) {
        this.index4 = this.langueges.length - 1;
      } else if (this.index5 < 0) {
        this.index5 = this.langueges.length - 1;
      }
    },
    async regUser() {
      let res = await axios.get(`/users-reg`)
      this.usersReg = res.data.regs
    }
  },
  mounted() {
    this.regUser()
  }
}
</script>

<template>
  <div class="pagecenter">
    <hr class="hr-start">
    <p class="center-desc">Здесь вы можете задать вопросы по таким языкам <br> программирования как</p>
    <div class="languages">
      <button @click="prevLang" class="btn-arrow leftarrow">&lt;</button>
      <div class="lang-items">
        <a :href="`/Forum?lang=${links[index]}`">
          <div class="lang-item lang-item-col-1" :class="stylesLang[index]">{{ langueges[index] }}</div>
        </a>
        <a :href="`/Forum?lang=${links[index1]}`">
          <div class="lang-item lang-item-col-2" :class="stylesLang[index1]">{{ langueges[index1] }}</div>
        </a>
        <a :href="`/Forum?lang=${links[index2]}`">
          <div class="lang-item lang-item-col-3" :class="stylesLang[index2]">{{ langueges[index2] }}</div>
        </a>
        <a :href="`/Forum?lang=${links[index3]}`">
          <div class="lang-item lang-item-col-4" :class="stylesLang[index3]">{{ langueges[index3] }}</div>
        </a>
        <a :href="`/Forum?lang=${links[index4]}`">
          <div class="lang-item lang-item-col-5" :class="stylesLang[index4]">{{ langueges[index4] }}</div>
        </a>
        <a :href="`/Forum?lang=${links[index5]}`">
          <div class="lang-item lang-item-col-6" :class="stylesLang[index5]">{{ langueges[index5] }}</div>
        </a>
      </div>
      <button @click="nextLang" class="btn-arrow rightarrow">&gt;</button>
    </div>
    <div class="wehave">
      <p class="wehave-title">В данный момент на нашем сайте:</p>
      <div class="wehave-items">
        <div class="wehave-item">
          <img src="../../assets/Main/user1.png" class="img-lox"style="width: 40px;" alt="">
          <p class="wehave-item-desc">Зарегистрированно <br> {{ this.usersReg }} пользователей</p>
        </div>
        <div class="wehave-item">
          <img src="../../assets/Main/expert.png" alt="">
          <p class="wehave-item-desc">5 экспертов в сети <br> и помогают сейчас</p>
        </div>
        <div class="wehave-item">
          <img src="../../assets/Main/users.png" alt="">
          <p class="wehave-item-desc">10 участников <br> онлайн</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@import url('https://fonts.cdnfonts.com/css/rubik');

html,
body {
  font-family: 'rubik';
}

#app {
  font-family: 'rubik';
}

body {
  margin: 5px;
}

hr {
  margin-top: 20px;
}

.pagecenter {
  height: 500px;
}

.center-desc {
  text-align: center;
  font-size: 24px;
}

.languages {
  margin-top: 40px;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
  height: 80px;
}

.lang-items {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 50px;
}

.lang-item {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  width: 135px;
  height: 60px;
  transition: 300ms;
  user-select: none;
  cursor: pointer;
}


.ts {
  background-color: #017ACC;
  color: #fff;
  font-weight: 600;
}


.ts:active {
  background-color: #004877;
}

.php {
  background-color: #777BB3;
  color: #000;
  font-weight: 600;
}


.php:active {
  background-color: #42446b;
}

.py {
  background-color: #3773A5;
  color: #fff;
  font-weight: 600;
}


.py:active {
  background-color: #214562;
}

.js {
  background-color: #FFE500;
  color: #000;
  font-weight: 600;
}


.js:active {
  background-color: #a19100;
}

.cs {
  background-color: #7455DC;
  color: #fff;
  font-weight: 600;
}


.cs:active {
  background-color: #433081;
}

.ruby {
  background-color: #A51501;
  color: #fff;
  font-weight: 600;
  /* -webkit-text-stroke: 0.5px black; */
}


.ruby:active {
  background-color: #670c00;
}

.go {
  background-color: #3be6e6;
  color: #000;
  font-weight: 600;
}


.go:active {
  background-color: #1bafaf;
}

.cpp {
  background-color: #3b71e6;
  color: #fff;
  font-weight: 600;
}


.cpp:active {
  background-color: #1e49a7;
}

.ja {
  background-color: #c00909;
  color: #fff;
  font-weight: 600;
}


.ja:active {
  background-color: #7e0b0b;
}

.ko {
  background-color: #9429eb;
  color: #fff;
  font-weight: 600;
}


.ko:active {
  background-color: #5e1997;
}

.btn-arrow {
  color: #646464;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 52px;
  width: 25px;
  height: 25px;
  background: none;
  border: none;
  transition: 100ms;
  user-select: none
}


.btn-arrow:active {
  color: #171717;
}

.wehave {
  margin-top: 40px;
}

.wehave-title {
  text-align: center;
  font-size: 22px;
  margin-bottom: 50px;
}

.wehave-item img {
  width: 50px;
  user-select: none;
}

.wehave-item {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 250px;
  height: 150px;
  padding-top: 10px;
  transition: 150ms;
  cursor: pointer;
  border-radius: 30px;
}


.wehave-item-desc {
  text-align: center;
}

.wehave-items {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}

.wehave p {
  user-select: none;
}


@media (max-width: 1225px) {
  .lang-item {
    width: 90px;
    height: 50px;
  }

  hr {
    width: 100%;
  }
}

@media (max-width: 950px) {
  .languages {
    gap: 10px;
  }

  .lang-items {
    gap: 10px
  }

  .lang-item-col-5,
  .lang-item-col-6 {
    display: none;
  }
}

/* @media (max-width: 870px) {
        .pagecenter {
            margin-top: -80px;
        }
    }
    @media (max-width: 770px) {
        .pagecenter {
            margin-top: -140px;
        }
    } */
@media (max-width: 680px) {
  .lang-items {
    flex-basis: 50%;
  }

  .lang-item-col-3,
  .lang-item-col-4,
  .lang-item-col-5,
  .lang-item-col-6 {
    display: none;
  }

}

@media (hover: hover) {
  .lang-item:hover {
    transition: all 300ms;
    transform: scale(1.4);
  }

  .ts:hover {
    background-color: #005e9d;
  }

  .php:hover {
    background-color: #5c5f91;
  }

  .py:hover {
    background-color: #2a587e;
  }

  .js:hover {
    background-color: #c4b000;
  }

  .cs:hover {
    background-color: #5a42aa;
  }

  .ruby:hover {
    background-color: #800f00;
  }

  .go:hover {
    background-color: #1fbebe;
  }

  .cpp:hover {
    background-color: #2954b3;
  }

  .ja:hover {
    background-color: #990b0b;
  }

  .ko:hover {
    background-color: #741dbb;
  }

  .btn-arrow:hover {
    color: #363636;
  }

  .wehave-item:hover {
    background-color: #ededed;
    box-shadow: 0px 0px 20px #c2c2c2;
  }

}

@media (max-width: 590px) {
  /* .languages {
      margin-bottom: 110px;
  } */
}

@media (max-width: 388px) {
  /* .languages {
      margin-bottom: 100px;
  } */
  .lang-item-col-2,
  .lang-item-col-3,
  .lang-item-col-4,
  .lang-item-col-5,
  .lang-item-col-6 {
    display: none;
  }
}

@media (min-width: 1750px) {
  .center-desc {
    font-size: 34px;
  }

  .lang-item {
    width: 160px;
    height: 70px;
    font-size: 24px;
  }
  
  .wehave-title {
    font-size: 34px;
  }
  
  .wehave-item {
    width: 400px;
    height: 200px;
  }
  
  .wehave-item-desc {
    font-size: 28px;
  }
  
  .wehave-item img {
    width: 80px;
  }

  .img-lox {
    width: 60px !important;
    margin-top: 20px;
  }
}

@media (min-width: 2600px) {
  .center-desc {
    font-size: 46px;
  }

  .lang-item {
    width: 220px;
    height: 100px;
    font-size: 32px;
  }

  .wehave-title {
    font-size: 46px;
  }

  .wehave-item-desc {
    font-size: 32px;
  }
}

@media (min-width: 3800px) {
  .center-desc {
    font-size: 56px;
  }

  .lang-item {
    width: 350px;
    height: 140px;
    font-size: 45px;
    border-radius: 22px
  }

  .wehave {
    margin-top: 100px;
  }

  .wehave-title {
    font-size: 60px;
  }

  .wehave-item {
    width: 600px;
    height: 300px;
  }

  .wehave-item img {
    width: 150px;
  }

  .img-lox {
    width: 130px !important;
  }

  .wehave-item-desc {
    font-size: 43px;
  }

  .leftarrow {
    font-size: 70px;
  }

  .rightarrow {
    font-size: 70px;
  }

  .languages {
    gap: 100px
  }

  .lang-items {
    gap: 100px;
  }

  .hr-start {
    margin-top: 0 !important;
  }
}
</style>
