package com.saikat.example.predictionofdisease.restcontroller;

import org.springframework.web.bind.annotation.RestController;
import com.saikat.example.predictionofdisease.entity.symptoms;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
public class simpleRestController {

    //@CrossOrigin(origins = "http://localhost:4200")
    @CrossOrigin(origins = "https://disease-predictor-frontend.vercel.app")
    @GetMapping("/em")
    public symptoms getMethodName() {
        symptoms s=new symptoms();
        s.setSymList("Hello Guys!");
        return s;
    }

    //@CrossOrigin(origins = "http://localhost:4200")
    @CrossOrigin(origins = "https://disease-predictor-frontend.vercel.app")
    @PostMapping("/em")
    public symptoms postMethodName(@RequestBody symptoms inputData) throws IOException, InterruptedException{

       
        // Build the command to call the Python script
        ProcessBuilder pb = new ProcessBuilder("python", "C:\\Users\\Saikat Moi\\Downloads\\JavaSpringBoot\\predictionofdisease\\src\\main\\python\\prediction_script.py", inputData.getSymList());
        pb.redirectErrorStream(true);

        // Start the Python script
        Process p = pb.start();
        p.waitFor();

        // Read the output from the Python script
        BufferedReader bfr = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String line;
        StringBuilder pythonOutput = new StringBuilder();

        while ((line = bfr.readLine()) != null) {
            pythonOutput.append(line).append("");
        }

        String result=pythonOutput.toString();
        symptoms s=new symptoms();
        s.setSymList(result);
        return s;
        //return "hello";
    }

}
