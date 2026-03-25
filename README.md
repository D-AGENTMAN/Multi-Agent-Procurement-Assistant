# Multi-Agent Procurement Assistant using CrewAI 🚀

## 📌 Overview

This project demonstrates a **multi-agent AI system** built using CrewAI to automate key procurement workflows including supplier discovery, quote analysis, risk assessment, and final decision-making.

The system mimics how a real procurement team operates—by assigning specialized roles to different AI agents and orchestrating them into a structured workflow.

---

## 💡 Problem Statement

Procurement teams often spend significant time on:

* Identifying and evaluating suppliers
* Comparing supplier quotes (pricing, MOQ, lead time)
* Assessing supplier risks
* Creating final recommendation reports

These tasks are **manual, time-consuming, and repetitive**.

---

## 🤖 Solution

A **multi-agent procurement assistant** that automates the end-to-end sourcing workflow using AI agents with distinct responsibilities.

---

## 🧠 Agents & Responsibilities

### 1. Supplier Research Specialist

* Uses web search (Serper API)
* Identifies and evaluates potential suppliers globally
* Gathers supplier capabilities and market presence

---

### 2. Procurement Analyst

* Reads and analyzes supplier quote files
* Compares:

  * Pricing
  * Minimum Order Quantity (MOQ)
  * Lead times
* Identifies cost-effective sourcing options

---

### 3. Supply Chain Risk Analyst

* Performs external risk assessment using web search
* Evaluates:

  * Financial stability
  * Geopolitical risks
  * Certifications & compliance

---

### 4. Procurement Report Writer

* Synthesizes all agent outputs
* Generates a **professional procurement report**
* Provides final supplier recommendations

---

## 🔄 Workflow

Supplier Research → Quote Analysis → Risk Assessment → Final Procurement Report

This structured workflow ensures **data-driven and risk-informed sourcing deci**
