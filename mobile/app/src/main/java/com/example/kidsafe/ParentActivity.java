package com.example.kidsafe;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import java.util.Objects;

public class ParentActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_parent);
        Objects.requireNonNull(getSupportActionBar()).setTitle("Menu");
    }


    @Override
    public void onBackPressed() {
    }
}