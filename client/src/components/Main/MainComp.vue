<script>
import PageStart from './PageStart.vue';
import PageCenter from './PageCenter.vue';
import PageEnd from './PageEnd.vue';
export default {
    components: {
        PageCenter,
        PageStart,
        PageEnd,
    }
}
</script>

<template>
<PageStart/>
<PageCenter/>
<PageEnd/>
</template>

<style scoped>



</style>