package com.saikat.example.predictionofdisease.entity;

import org.springframework.stereotype.Component;

@Component
public class symptoms {
private String symList;
public symptoms(){}
public String getSymList() {
    return symList;
}
public void setSymList(String symList) {
    this.symList = symList;
};



}
