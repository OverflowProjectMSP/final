<script>
import axios from 'axios';
// import VidComp from './components/MainComponents/VidComp.vue'
import ModelWind from '../ReuseComponets/ModelWind.vue';
import VidjetComp from '../ReuseComponets/StateVid.vue';
export default {
    components: {
    // VidComp,
        ModelWind,
        VidjetComp  
    },
    data() {
        return {
            states: [],
            Show: false,
            tag: ``,

            title: ``,
            author: ``,
            cnt: 0
        }
    },
    methods: {
        OpenModal() {
            this.Show = !this.Show
        },
        CloseModal(Show) {
            this.Show = false
        },
        async loadStates() {
            let res = await axios.get('/show-states');
            this.states = res.data.all;
            this.cnt++
            // console.log(res.data)
        },

        async searchStates() {
            let res = await axios.get('/search', {
                params: {
                    title: this.title,
                    author: this.author,
                }
            });
            this.states = res.data.all;
        },

        async filtre() {
            let res = await axios.get('/filtre-states', {
                params: {
                    title: this.title,
                    author: this.author,
                    tag: this.tag,
                }
            });
            this.states = res.data.all;
        },
    },
    mounted() {
        this.loadStates()
    },
}
</script>

<template>
<!-- Компонент поиска -->
<h4 class="text">Поиск статьи</h4>

<div class="content d-flex align-items-center">
    <input v-model="title" type="search" class="form-control" placeholder="Название статьи" aria-label="First name">
    <input v-model="author" type="search" class="form-control" placeholder="Автор" aria-label="Last name">
   <!-- селект -->
  <div class="down-menu d-flex align-items-center">
      <div class="dropdown-center">
        <select class="form-select me-2" v-model="tag">
            <option value="javascript">JavaScript</option>
            <option value="ts">TS</option>
            <option value="python">Python</option>
            <option value="php">PHP</option>
            <option value="cpp">C++</option>
            <option value="java">Java</option>
            <option value="cs">C#</option>
            <option value="go">Golang</option>
            <option value="IB">ИБ</option>
            <option value="">Без фильтров</option>
        </select>
      </div>
      <!-- плюсик -->
      <div class="contain" @click="OpenModal" >
        <img src="../../assets/States/add.png" class="add" alt="">
      </div>
      <button class="btn find-btn btn-outline-primary  ms-4" @click="filtre">Отфильровать</button>

      </div>
  </div>




<!-- Див с виджетами -->
<div class="conr">
    <div class="con" v-for="item in states">
        <a :href="`/StateItem/` + item.id">
            <!-- <vid-comp :item="item" role="button" /> -->
            <vidjet-comp :item="item"    />
        </a>
    </div>
</div>
<div class="content p-2" v-if="this.states.length == 0 && this.cnt == 1">
    <h2 class="d-flex justify-content-center my-5 user-select-none">Будь первым, кто даст ответ на этот вопрос!</h2>
</div>

<model-wind v-if="Show" @CloseModal="CloseModal"/>


</template>

<style scoped>
.find-btn{
    color: black;
}
.conr{
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: scroll; 
    overflow-x: hidden;
    height: 555px;
    padding-top: 10px;
    /* width: auto;
    margin-left: auto;
    margin-right: auto; */
}
a {
    text-decoration: none;
    color: #000;
}
h4{
    margin-left: 20.5%;
    margin-top: 20px;
    font-size: 40px;
    
}
.image{
    margin-right: 10px;
    width: 25px;
}
.add{
    width: 25px;
    height: 25px;
    cursor: pointer
}
.btn{
    font-size: 16px;
    font-weight: bold;
    color:rgb(0, 0, 0) ;
}
.content {
    margin: 10px;
    flex-wrap: wrap;
    margin-left: 20%;
    /* margin-bottom: 100px; */
}
.form-control{
    margin: 5px;
}
.dropdown-center{
    margin-left: 15px;
}
.content input{
    width: 300px;
    border-radius: 10px;
}
.con{
    width: 750px;
    /* justify-content: start; */
    /* display: flex; */
}

/* .con a {
    width: 100px !important;
} */

.contain{
    width: 5%;
    height: 5%;
    
}
.plus {
    width: 30px; 
    height: 30px;
    background-color: #e8e7ea;
    border-radius: 50%; 
    border: 0.0001px solid ; 
    
    
   
}
.p{
    margin-left: 0.2px;
    margin-right: 1px;
}
.dropdown-center{
    margin-right:10px;
}

@media (hover: hover) {
    .find-btn:hover{
        color: white;
        transition: all 0.5s;
    }
}

/* @media (min-width: 1900px) {
    .con {
        width: 1300px
    }
    
    .con a {
        width: 1000px !important;
    }
} */

@media (max-width: 900px){

.content input{
    width: 200px;
}
.content, h4 {
    margin-left: 100px;
    margin-right: 100px;
}
.dropdown-center{
    margin: 2px !important;
}
}
@media (max-width: 800px) {
    .content, h4 {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    h4 {
        font-size: 30px;
    }
}
@media (max-width: 635px) {
  .content .form-control{
    width: 400px;
   }
}
</style>
