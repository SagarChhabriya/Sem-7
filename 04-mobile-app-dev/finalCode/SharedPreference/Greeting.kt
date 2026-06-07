package com.example.sharedpeferences

import android.content.Context
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext

@Composable
fun Greeting() {
    val context = LocalContext.current
    val sharedPreferences =
        context.getSharedPreferences("MyPrefs", Context.MODE_PRIVATE)

    val name = sharedPreferences.getString("name", "Guest")

    Box(
        modifier = Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        Text(
            text = "Hello $name!",

        )
    }
}
