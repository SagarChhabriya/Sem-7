package com.example.statemanagement



import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.ViewModel

class MainViewModel : ViewModel() {

    // State
    var name = mutableStateOf("")

    // Function to update state
    fun updateName(newName: String) {
        name.value = newName
    }
}
