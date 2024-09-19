<script>
import PageStart from './PageStart.vue';
import PageCenter from './PageCenter.vue';
import PageEnd from './PageEnd.vue';
import ScrollBarComp from './ScrollBarComp.vue';
import HeaderComp from '../ReuseComponets/HeaderComp.vue';
import NewHeader from '../Edit/NewnavBar.vue'
export default {
    components: {
        HeaderComp,
        PageCenter,
        PageStart,
        PageEnd,
        ScrollBarComp,
        NewHeader,
    },
}
</script>

<template>
    <!-- <HeaderComp /> -->
<PageStart/>
<PageCenter/>
<PageEnd/>
<ScrollBarComp/>
</template>

<style scoped>



</style>
