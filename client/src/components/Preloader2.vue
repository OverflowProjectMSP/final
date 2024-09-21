<script>
export default {
    data() {
        return {
            show: true,
        }
    },
    methods: {
        setShow() {
            setTimeout(() => {
                this.show = false
            }, 1000)
        }
    },
    mounted() {
        this.setShow();
        // setInterval(()=> {this.$emit('setShow', this.show)}, 1000)
    }
}
</script>

<template>
    <!-- <div class="container" v-if="false">
        <div class="load-item item1"></div>
        <div class="load-item item2"></div>
        <div class="load-item item3"></div>
        <div class="load-item item4"></div>
        <div class="load-item item5"></div>
    </div> -->
    
            <div class="container"><img src="../assets/preloader.svg" alt="" class="img"></div> 
</template>

<style scoped>
.img{
    width: 100px;
    height: 100px;
}
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 60vh;
    margin-left: 40px;
}

.load-item {
    width: 15px;
    height: 15px;
    background-color: #4200FF;
}

.item1 {
    animation: expand 0.4s infinite alternate;
}

.item2 {
    animation: expand 0.4s infinite alternate;
}

.item3 {
    animation: expand 0.4s infinite alternate;
}

.item4 {
    animation: expand 0.4s infinite alternate;
}

.item5 {
    animation: expand 0.4s infinite alternate 200ms;
}

@keyframes expand {
  0% {
    height: 15px;
  }
  100% {
    height: 40px;
  }
}
</style>
