<script>
import PageStart from './PageStart.vue';
import PageCenter from './PageCenter.vue';
import PageEnd from './PageEnd.vue';
import ScrollBarComp from './ScrollBarComp.vue';
export default {
    components: {
        PageCenter,
        PageStart,
        PageEnd,
        ScrollBarComp,
    }
}
</script>

<template>
<PageStart/>
<PageCenter/>
<PageEnd/>
<ScrollBarComp/>
</template>

<style scoped>



</style>