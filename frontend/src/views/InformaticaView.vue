<template>
    <div>
        <p>{{ result }}</p>
        <img src = "../assets/qrcodes/informatica/qrcode.png"/>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'informatica',
    data: () => ({
        timer: null,
        result: "Informatica"
    }),
    // methods: {
    //     getMessage() {
    //         const URL = 'http://localhost:5000/entrance'
    //         axios.get(URL).then(response => this.result = response.data)
    //     }
    // },
    // mounted() {
    //     this.getMessage()
    // }
}
</script>