<template>
    <div>
    {{ test }}
    </div>
</template>


<script>
    export default {
        data () {
            return {
                test: 'Start. Fetch message in 2 seconds'
            }
        },
        created () {
            setTimeout(() => {
                console.log('GO')
                this.$http.get('http://52.232.81.235:5000/test').then( (response) => {
                    console.log(response)
                    this.test = response.body.tasks[0].msg
                });
            }, 2000)
        }
    }
</script>