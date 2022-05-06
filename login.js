console.log("inside current log_in.js")
// Create a new Vue instances
const main = Vue.createApp({
        // Data Properties
    data() {
        return {
            errors: [],
            input_email: null,
            input_password: null
        }
    },


methods:{
    checkForm:function(){
        if(this.input_email && this.input_password){
            this.validate()
        }
        this.errors = []
        if(!this.input_email){
            this.errors.push("Enter your email in the format \"user@domain\".")
        }
        else if(!this.input_password){
            this.errors.push("Enter your password.")
        }
    },

    validateForm(){
        this.errors = []
        this.errors.push("Either Email or Password is wrong.")
    },

    validate(){
        console.log("=== start validate() ===")
        localStorage.setItem('email', this.input_email)
        // console.log(localStorage.getItem('email')) //using this to retrieve the email
        let url = "../backend/verifyStudent.php?student_email=" + this.input_email + "&password=" + this.input_password

        axios.get(url)
        .then((response) => {
            console.log(response)
            if(response.data == 'wrong email or password'){
                this.validateForm()
            }
            else{
                window.location.href = "./searchBooking.html"
            }
        })
        .catch(error =>{
            console.log('not found')
            console.log(error.message)
        })
    }

}

})

main.mount("#main")