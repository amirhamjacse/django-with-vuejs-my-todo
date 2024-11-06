<template>
    <div>
        <h2 class="alert alert-primary">{{msg}} Calculator</h2>
        <input class="form-control py-1 my-1" type="text" v-model="first_number">
        <input class="form-control py-1 my-1" type="text" v-model="second_number">
        <button class="btn btn-success" @click="sumofTwonum()">Get result</button>
        <h3>Result: {{ result }}</h3>
        <button class="btn btn-success" @click="getTaskData()">Call Api</button>
        <p>{{ task_data.title }}</p>
        <!-- <p>{{ task_data.id }}</p>
        <p>{{ task_data.userId }}</p> -->
        <!-- <p v-for="task in task_data">
            
        </p> -->
        

    </div>
</template>

<script>
import axios from 'axios';
export default{
    data(){
        return{
            msg: 'Number',
            first_number: '',
            second_number: '',
            result: '',
            task_data: [],
        }
    },
    mounted(){
        this.getTaskData();
    },
    methods:{
        sumofTwonum(){
            this.first_number = parseInt(this.first_number)
            this.second_number = parseInt(this.second_number)
            this.result = this.first_number + this.second_number
            // console.log('working', this.result)
        },
        async getTaskData(){
            const response = await axios.get('https://jsonplaceholder.typicode.com/todos/1');
            this.task_data = response.data;
            console.log(response.data);
        },

    }
}

</script>

<style>

</style>