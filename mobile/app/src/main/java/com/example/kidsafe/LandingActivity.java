package com.example.kidsafe;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Objects;


public class LandingActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_landing);
        Objects.requireNonNull(getSupportActionBar()).hide();


        Button join = findViewById(R.id.materialButton);

        Button joinParent = findViewById(R.id.materialButton2);

        Button joinTeacher = findViewById(R.id.materialButton3);

        join.setOnClickListener(view -> startActivity(new Intent(LandingActivity.this, SignUpActivity.class)));

        joinParent.setOnClickListener(view -> startActivity(new Intent(LandingActivity.this, SignUpParentActivity.class)));

        joinTeacher.setOnClickListener(view -> startActivity(new Intent(LandingActivity.this, SignUpTeacherActivity.class)));

        Button login = findViewById(R.id.materialButton1);

        login.setOnClickListener(view -> startActivity(new Intent(LandingActivity.this, LoginActivity.class)));


        SharedPreferences sharedPreferences = getSharedPreferences("MySharedPref", MODE_PRIVATE);
        SharedPreferences.Editor myEdit = sharedPreferences.edit();

        myEdit.putString("HOST_ADR", "http://192.168.100.20:5000");
        myEdit.apply();

    }
}
