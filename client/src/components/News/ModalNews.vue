<script>
export default {
  data() {
		return {

		}
	},

	props: {
		news: Array
	}
};
</script>

<template>
<div class="flex">
	<div class="news-container border border-4 border-black rounded-5 p-4">
		<img @click='this.$emit(`closeNews`)' class="btn-close" src="../../assets/FAQ/close.svg" alt="Close">
		<div class="card" v-for='item in news'>
			{{ item }}
		</div>
	</div>
</div>
 
</template>

<style scoped>
.news-container {
	position: fixed;
	top: 5%;
	width: 90%;
	left: 5%;
	height: 90%;
	z-index: 333;
	background-color: #fff;
}

.btn-close {
	position: absolute;
	top: 15px;
	right: 15px;
	cursor: pointer;
}
</style>