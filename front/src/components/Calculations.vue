<template>
    <v-card class="cacl-card" outlined >
        <v-card-subtitle>{{ config.name.toUpperCase() }} </v-card-subtitle>
        <v-card-text>
            <v-col>
            <v-form>
<!--                <v-row align="center">-->
<!--                <v-col sm="6" md="3">-->
                    <v-text-field outlined
                                  v-for="param in config.params"
                                  v-bind:key="param.name"
                                  :v-model="param.name + '_value'"
                                  :label="param.name"
                                  :ref="param.name"
                                  :type="param.type"
                                  :rules="[rules.required, rules.int]"
                    />
                    <v-btn depressed :disabled="Boolean(ready)" color="primary" @click.prevent="submit">Run</v-btn>
<!--                </v-col>-->

<!--                </v-row>-->
            </v-form>
            </v-col>
        </v-card-text>
    </v-card>
</template>

<style lang="sass" scoped>
    .cacl-card
        margin-bottom: 40px
</style>

<script>
    import Vue from "vue"
    export default({
        name: 'App',
        props: ['title', 'config'],
        data: () => ({
            test: [],
            ready: false,
            rules: {
                required: value => !!value || 'Required.',
                int: value => {
                    const pattern = /^[0-9]+(\.[0-9]+)?$/
                    const valid = pattern.test(value)
                    return valid || 'Please type a valid numeric value'
                },
            },
        }),
        methods: {
            submit: async function () {
                // calc exec request here
                const resp = await Vue.http.get('http://localhost:8000/calculate/algo/')
                this.test = resp.data
                Object.keys(this.$refs).map(key=>{ console.log(key); console.log(this.$refs[key].value) })
            }
        }
    })
</script>