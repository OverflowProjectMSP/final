<script>
export default {
    data() {
        return {

        }
    }
}
</script>

<template>
    <div class="pageend">
        <h3 class="join-us-title">Присоединяйся к нам!</h3>
        <p class="join-us-desc">Ведь у нас ты можешь:</p>
        <div class="join-us-items">
            <div class="join-us-item"><button>Задавать вопросы</button></div>
            <div class="join-us-item"><button>Помогать новичкам</button></div>
            <div class="join-us-item"><button>Находить партнёров</button></div>
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

a {
    text-decoration: none;
}

.pageend {
    height: 300px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    margin-bottom: 0;
}

.join-us-title {
    text-align: center;
    font-weight: 400;
    font-size: 42px;
    margin: 0;
    margin-bottom: 10px;

}

.join-us-desc {
    font-size: 22px;
    margin: 0;
    margin-bottom: 60px;
}

.join-us-items {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 40px;
}

.join-us-item button {
    border: 1px solid #dae9fb;
    width: 250px;
    height: 50px;
    border-radius: 50px;
    border: none;
    background-color: #BFDBFE;
    cursor: pointer;
    font-size: 16px;
    transition: all 200ms;
}

@media (hover: hover) {
    .join-us-item button:hover {
        transform: scale(1.1);
        box-shadow: 0px 0px 20px #aac3e1;
        background-color: #aac3e1
    }
}

@media (max-width: 790px) {
    .pageend {
        margin-top: 150px;
    }
}
@media (max-width: 850px) {
    
         .pageend{
            margin-bottom: 80px;
        }
    
        @media (max-width: 540px) {
    
    .pageend{
       margin-bottom: 150px;
   }

}
@media (max-width: 450px) {
    
    .pageend{
       margin-bottom: 180px;
   }

}
}

@media (max-width: 589px) {
    .pageend {
        margin-top: 230px;
    }
}

@media (max-width: 529px) {
    /* .pageend {
        margin-top: 430px;
    } */
}

@media (max-width: 519px) {
    .pageend {
        margin-top: 400px;
    }
}

@media (max-width: 388px) {
    /* .pageend {
        margin-top: 600px;
    } */
}
</style>