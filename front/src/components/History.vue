<template>
    <p>
    {{ tasks }}
    </p>
</template>

<script>
    import Vue from 'vue'
    export default {
        data: () => ({
            tasks: []
        }),
        beforeCreate() {
            this.tasks = Vue.http.get('http://localhost:8000/calculations/')
        }
    }
</script>