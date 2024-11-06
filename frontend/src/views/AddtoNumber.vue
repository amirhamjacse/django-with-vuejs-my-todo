<template>
    <div>
        <h2 class="alert alert-primary">{{msg}} Calculator</h2>
        <input class="form-control py-1 my-1" type="text" v-model="first_number">
        <input class="form-control py-1 my-1" type="text" v-model="second_number">
        <button class="btn btn-success" @click="sumofTwonum()">Get result</button>
        <h3>Result: {{ result }}</h3>
    </div>
</template>

<script>
export default{
    data(){
        return{
            msg: 'Number',
            first_number: '',
            second_number: '',
            result: '',
        }
    },
    methods:{
        sumofTwonum(){
            this.first_number = parseInt(this.first_number)
            this.second_number = parseInt(this.second_number)
            this.result = this.first_number + this.second_number
            // console.log('working', this.result)
        }
    }
}

</script>

<style>

</style>