<script>
export default {
    data() {
        return {
            // user.avatar: "hebber.png",
            // user.username: "HaBy",
            // rang: "бывший дрочила",
            // tag: "JavaScript",
            // descriptions: "Я двойник Павла Дурова, у меня 3492784 детей, люблю мужчин по старше, обожаю францию и лягушек",
            // date: "9222 до н.э.",
            // acnt: 3,
        }
    },

    props: {
        data: Object,
    }
}
</script>

<template>
    <div class="window">
        <div class="vid-block">
            <div class="info">
                <div class="avatar-name-rank">
                    <div class="avatar">
                        <img v-if='this.data.user.avatar' :src="data.user.avatar" alt="">
                    </div>
                    <div class="name-rank" >
                        <h5 v-if='this.data.user.username' class="user-name">{{ data.user.username }}</h5>
                        <p>Звание: {{ data.rang }}</p>
                    </div>
                </div>
                <div class="language">
                    <p>{{ data.tag }}</p>
                </div>
                <div class="text">
                    <p>{{ data.descriptions }}</p>
                </div>
                <div class="date">
                    <p>{{ data.date }}</p>
                </div>
            </div>
            <div class="answers">
                <div class="count-ans">
                    <p class="count">{{ data.acnt }}</p>
                    <p class="ans">Ответа (ов)</p>
                </div>
                
                <button>Ответить</button>
            </div>
        </div>
    </div>
</template>

<style>
p {
    margin: 0;
}

.window {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 100%;
    height: 100%;

    margin-left: 0px;
}

.count-ans {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.vid-block {
    display: flex;
    justify-content: space-between;
    
    margin: 0 10px;

    width: 900px;
    height: auto;
    border: 2px solid #000;
    border-radius: 20px;

    transition: all 300ms;
}

.vid-block:hover {
    transform: translateY(-10px);
    box-shadow: 10px 5px 5px rgb(0, 0, 0, 0.5);
}

.info {
    display: flex;
    flex-direction: column;
    margin-left: 15px;
    gap: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
}

.name-rank p {
    padding-left: 0 !important;
    padding-right: 0 !important;
}

.avatar img {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border-radius: 50px;
    border: 2px solid #000;
}

.avatar-name-rank {
    display: flex;
    align-items: center;
    gap: 15px;
}

.name-rank {
    display: flex;
    flex-direction: column;
}

.user-name {
    margin: 0;
}

.language p {
    color: #A339FF;
    font-weight: 600;
}

.text p {
    font-size: 22px;
    font-weight: 500;

    width: 45ch;
    overflow: hidden;
    white-space: nowrap;
    /* V2 */
    /* white-space: wrap; */
    text-overflow: ellipsis;
}

.date p {
    color: #3382FF;
    font-weight: 600;
}

.answers {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    width: 200px;
    height: auto;
    /* border: 1px solid #000; */
}

.answers p {
    font-size: 20px;
    font-weight: 600;
    opacity: 0.6;
}

.answers button {
    color: #fff;
    background-color: #3382FF;
    border: none;
    border-radius: 12px;

    font-size: 20px;
    font-weight: 600;

    padding: 6px 20px;

    margin-top: 15px;

    transition: all 100ms;
}

.answers button:hover {
    background-color: #2e6ac9;
}



/* АДАПТИВКА */

@media (max-width: 900px) {
    .vid-block {
        width: 650px;
    }

    .text p {
        width: 25ch;
    }
}

@media (max-width: 650px) {
    .vid-block {
        flex-direction: column;
        width: 400px;
        position: relative;
        height: 250px;
    }

    .answers {
        width: 150px;
        height: 150px;
        display: flex;
        flex-direction: row;
        
        position: absolute;
        top: 130px;
        left: 100px;
        gap: 40px;
    }

    .count-ans {
        align-items: center;
    }

    .count-ans .count {
        margin-left: 80px;
    }

    .answers p {
        width: 120px;
    }

    .text {
        width: 100%;
        height: 66px;
    }

    .date {
        margin-bottom: 100px;
    }

    .text p {
        -webkit-line-clamp: 2;
        line-clamp: 2;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        overflow: hidden;
        white-space: wrap;
        width: 26ch;
        
    }

    .name-rank p {
        font-size: 14px;
    }
}

@media (max-width: 400px) {
    .vid-block {
        width: 300px;
    }

    .text p {
        font-size: 20px;
        width: 20ch;
    }

    .answers {
        top: 140px;
        gap: 5px;

    }

    .count-ans {
        margin-left: -70px;
        width: 150px;
    }
    
    .answers p {
        font-size: 16px;
    }

    .answers button {
        font-size: 16px
    }

    .date p {
        font-size: 12px
    }
}
</style>
