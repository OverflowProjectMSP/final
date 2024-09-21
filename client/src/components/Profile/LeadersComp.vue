<script>
import axios from 'axios';

export default {
    data() {
        return {
            topLeader: [
                // {
                //     username: `Олег`,
                //     rang: `Мастер`,
                //     answers: 102
                // },
                // {
                //     username: `Генадий`,
                //     rang: `Остолоб`,
                //     answers: 53
                // },
                // {
                //     username: `Кирилл`,
                //     rang: `ИИ`,
                //     answers: 12
                // },
                // {
                //     username: `Олег`,
                //     rang: `Мастер`,
                //     answers: 101
                // },
                // {
                //     username: `Генадий`,
                //     rang: `Остолоб`,
                //     answers: 51
                // },
                // {
                //     username: `Кирилл`,
                //     rang: `ИИ`,
                //     answers: 10
                // },
                // {
                //     username: `Олег`,
                //     rang: `Мастер`,
                //     answers: 107
                // },
                // {
                //     username: `Генадий`,
                //     rang: `Остолоб`,
                //     answers: 50
                // },
                // {
                //     username: `Кирилл`,
                //     rang: `ИИ`,
                //     answers: 19
                // },
                // {
                //     username: `Генадий`,
                //     rang: `Остолоб`,
                //     answers: 42
                // },
            ],
            bgi: `#fff`,
            result: null,
            answ: [],
            index: 0
        }
    },
    mounted() {
        this.loadLeaders();
    },
    methods: {
				async loadLeaders() {
					let res = await axios.get('/get-top');
					this.topLeader = res.data.all;
					this.result = this.topLeader.sort((a, b) => b.answers - a.answers);
				}
    }
}
</script>

<template>
    <div class="containera d-flex flex-column border border-dark rounded-top-4 px-0 pb-0 my-4" >
        <h2 class="w-100 bg-primary text-white p-3 rounded-top-4 text-center">Таблица лидеров</h2>
        <ol class="ps-0 my-0">
            <li class="p-2 border-bottom border-dark d-flex justify-content-between flex-row align-items-center gap-2 w-100"
                v-for="(leader, index) in result" :style="{ 'background': bgi }">
                <div class="card-leader d-flex flex-row gap-3 align-items-center">
                    <h3 class="ps-2">{{ index + 1 }}.</h3>
										<img @click='this.$router.push(`/Profile/${leader.id}`)' :src="leader.avatar" class="rounded-circle">
                    <div class="main-info d-flex flex-column">
                        <h4 @click='this.$router.push(`/Profile/${leader.id}`)' class="mb-0">{{ leader.username }}</h4>
                        <span class="text-muted">Гений</span>
                    </div>
                </div>
                <span class="fs-4">{{ leader.total_count }} <span class="ans">Ответов</span></span>
            </li>
        </ol>
    </div>
</template>

<style scoped>
.card-leader img {
	width: 50px;
	height: 50px;
	object-fit: cover;
	cursor: pointer;
}

.containera {
		margin: 20px 300px !important;
	}

ol li:nth-child(1) {
    background-color: #a0cbff !important;
}

ol li:nth-child(2) {
    background-color: #BFDBFE !important;
}

ol li:nth-child(3) {
    background-color: #dbebff !important;
}

h2 {
    margin-bottom: 0 !important;
}

.main-info h4 {
	cursor: pointer;
	transition: color 300ms;
	word-break: break-all;
}

.main-info h4:hover {
	color: #0d6efd;
}

@media (max-width: 1144px) {
	.ans {
		display: none;
	}

	.containera {
		margin: 20px 20px !important;
	}
}
</style>