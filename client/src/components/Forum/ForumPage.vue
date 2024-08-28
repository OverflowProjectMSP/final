<script>
import axios from 'axios';
</script>

<template>
<div class="container d-flex flex-column gap-2 align-items-center mt-5">
    <h2 class="text-center mt-3">Выберите язык:</h2>
    <a href="/Forum/javascript"><button class="btn btn-outline-primary">JavaScript</button></a>
    <a href="/Forum/python"><button class="btn btn-outline-primary">Python</button></a>
    <a href="/Forum/cs"><button class="btn btn-outline-primary">C#</button></a>
    <a href="/Forum/ts"><button class="btn btn-outline-primary">TypeScript</button></a>
    <a href="/Forum/go"><button class="btn btn-outline-primary">Go</button></a>
    <a href="/Forum/java"><button class="btn btn-outline-primary">Java</button></a>
    <a href="/Forum/cpp"><button class="btn btn-outline-primary">C++</button></a>
    <a href="/Forum/kotlin"><button class="btn btn-outline-primary">Kotlin</button></a>
    <a href="/Forum/ruby"><button class="btn btn-outline-primary">Ruby</button></a>
    <a href="/Forum/php"><button class="btn btn-outline-primary">PHP</button></a>
    <a href="/Forum/design" class="mb-3"><button class="btn btn-outline-primary">Design</button></a>
</div>  
</template>

<style scoped>
.container {
    min-height: 60.7vh;
}
.a{
    margin-bottom: 30px;
}
a, button {
    width: 320px !important;
}
</style>
