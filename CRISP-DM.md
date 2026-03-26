# CRISP-DM: CRoss-Industry Standard Process Model

**Discussion Paper — March 1999**

**Authors:** Pete Chapman (NCR), Randy Kerber (NCR), Julian Clinton (SPSS), Thomas Khabaza (SPSS), Thomas Reinartz (DaimlerChrysler), Rüdiger Wirth (DaimlerChrysler)

> *This document, and information herein, are the exclusive property of the partners of the CRISP-DM consortium: NCR Systems Engineering Copenhagen (Denmark), DaimlerChrysler AG (Germany), Integral Solutions Ltd. (England) and OHRA Verzekeringen en Bank Groep B.V (The Netherlands). Copyright (C) 1999*

---

## Part I: Introduction

### 1. The CRISP-DM Methodology

#### 1.1 Hierarchical Breakdown

The CRISP-DM data mining methodology is described in terms of a hierarchical process model, consisting of sets of tasks described at four levels of abstraction (from general to specific):

1. **Phase** — At the top level, the data mining process is organized into a number of phases; each phase consists of several second-level generic tasks.

2. **Generic Task** — This second level is called generic because it is intended to be general enough to cover all possible data mining situations. The generic tasks are intended to be as complete and stable as possible. *Complete* means covering both the whole process of data mining and all possible data mining applications. *Stable* means that the model should be valid for yet unforeseen developments like new modelling techniques.

3. **Specialised Task** — The place to describe how actions in the generic tasks should be carried out in certain specific situations. For example, at the second level there might be a generic task called "clean data." The third level would describe how this task differed in different situations, such as cleaning numeric values versus cleaning categorical values, or whether the problem type is clustering or predictive modeling.

4. **Process Instance** — A record of the actions, decisions, and results of an actual data mining engagement. A process instance is organized according to the tasks defined at the higher levels, but represents what actually happened in a particular engagement, rather than what happens in general.

> **Note:** The description of phases and tasks as discrete steps performed in a specific order represents an idealised sequence of events. In practice, many of the tasks can be performed in a different order and it will often be necessary to repeatedly backtrack to previous tasks and repeat certain actions.

#### 1.2 Reference Model and User Guide

The CRISP-DM methodology distinguishes between the **Reference Model** and the **User Guide**:

- The **Reference Model** presents a quick overview of phases, tasks, and their outputs, and describes *what* to do in a data mining project.
- The **User Guide** gives more detailed tips and hints for each phase and each task within a phase and depicts *how* to do a data mining project.

### 2. Mapping Generic Models to Specialized Models

#### 2.1 Data Mining Context

Mapping between the generic and the specialized level in CRISP-DM is driven by the **Data Mining Context**. Four dimensions are distinguished:

1. **Application Domain** — The specific area in which the data mining project takes place.
2. **Data Mining Problem Type** — The specific class(es) of objective(s) which the data mining project deals with.
3. **Technical Aspect** — Specific issues in data mining which describe different (technical) challenges that usually occur during data mining.
4. **Tool and Technique** — Which data mining tool(s) and/or techniques are applied during the data mining project.

| Dimension | Examples |
|-----------|----------|
| Application Domain | Response Modeling, Churn Prediction, … |
| Data Mining Problem Type | Description and Summarization, Segmentation, Concept Description, Classification, Prediction, Dependency Analysis |
| Technical Aspect | Missing Values, Outliers, … |
| Tool and Technique | Clementine, MineSet, Decision Tree, … |

#### 2.2 Mappings with Contexts

Two different types of mapping between generic and specialized level:

1. **"Mapping for the Presence"** — Applying the generic process model to perform a single data mining project and mapping generic tasks to the specific project as required.
2. **"Mapping for the Future"** — Systematically specialising the generic process model according to a pre-defined context, or consolidating experiences of a single project towards a specialised process model for future usage in comparable contexts.

#### 2.3 How to Map?

The basic strategy for mapping the generic process model to the specialized level:

- Analyse your specific context
- Remove any details not applicable to your context
- Add any details specific to your context
- Specialize (or instantiate) generic contents according to concrete characteristics of your context
- Possibly rename generic contents to provide more explicit meanings in your context for clarity

### 3. Description of Parts

The CRISP-DM Process Model is organized into five parts:

- **Part I** — Introduction into the CRISP-DM methodology and general guidelines for mapping
- **Part II** — The CRISP-DM Reference Model: phases, generic tasks, and outputs
- **Part III** — The CRISP-DM User Guide: detailed advice including checklists
- **Part IV** — Concrete specifications of each output and its components, with template documents
- **Part V** — Appendix: glossary and characterization of data mining problem types

---

## Part II: The CRISP-DM Reference Model

The life cycle of a data mining project consists of **six phases**. The sequence of the phases is not strict — moving back and forth between different phases is always required. It depends on the outcome of each phase which phase, or which particular task of a phase, has to be performed next.

The cyclic nature of data mining means it is not over once a solution is deployed. The lessons learned during the process and from the deployed solution can trigger new, often more focused business questions. Subsequent data mining processes will benefit from the experiences of previous ones.

### 1. Business Understanding

This initial phase focuses on understanding the project objectives and requirements from a business perspective, and then converting this knowledge into a data mining problem definition and a preliminary plan designed to achieve the objectives.

#### 1.1 Determine Business Objectives

**Task:** The first objective of the data analyst is to thoroughly understand, from a business perspective, what the client really wants to accomplish. Often the client will have many competing objectives and constraints that must be properly balanced. The analyst's goal is to uncover important factors, at the beginning, that can influence the outcome of the project. A possible consequence of neglecting this step is to expend a great deal of effort producing the right answers to the wrong questions.

**Outputs:**

- **Background** — Details the information that is known about the organization's business situation at the beginning of the project.
- **Business Objectives** — Describe the customer's primary objective, from a business perspective. In addition to the primary business objective, there are typically a large number of related business questions that the customer would like to address.
- **Business Success Criteria** — Describe the criteria for a successful or useful outcome to the project from the business point of view. This might be quite specific (e.g., reduction of customer churn to a certain level) or general and subjective (e.g., "give useful insights into the relationships").

#### 1.2 Assess Situation

**Task:** This task involves more detailed fact-finding about all of the resources, constraints, assumptions, and other factors that should be considered in determining the data analysis goal and project plan.

**Outputs:**

- **Inventory of Resources** — List the resources available to the project, including: personnel (business experts, data experts, technical support, data mining personnel), data (fixed extracts, access to live warehoused or operational data), computing resources (hardware platforms), software (data mining tools, other relevant software).
- **Requirements, Assumptions, and Constraints** — List all requirements of the project including schedule of completion, comprehensibility and quality of results, and security as well as legal issues. List assumptions made by the project and constraints on the project.
- **Risks and Contingencies** — List the risks (events which might occur to delay the project or cause it to fail) and the corresponding contingency plans.
- **Terminology** — A glossary of terminology relevant to the project, including (1) a glossary of relevant business terminology and (2) a glossary of data mining terminology, illustrated with examples relevant to the business problem.
- **Costs and Benefits** — A cost-benefit analysis for the project; compare the costs of the project with the potential benefit to the business if it is successful.

#### 1.3 Determine Data Mining Goals

**Task:** A business goal states objectives in business terminology. A data mining goal states project objectives in technical terms. For example, the business goal might be "Increase catalog sales to existing customers" while a data mining goal might be "Predict how many widgets a customer will buy, given their purchases over the past three years, demographic information (age, salary, city, etc.), and the price of the item."

**Outputs:**

- **Data Mining Goals** — Describe the intended outputs of the project which will enable the achievement of the business objectives.
- **Data Mining Success Criteria** — Define the criteria for a successful outcome to the project in technical terms (e.g., a certain level of predictive accuracy, or a propensity to purchase profile with a given degree of "lift").

#### 1.4 Produce Project Plan

**Task:** Describe the intended plan for achieving the data mining goals, and thereby achieving the business goals. The plan should specify the anticipated set of steps to be performed during the rest of the project including an initial selection of tools and techniques.

**Outputs:**

- **Project Plan** — List the stages to be executed in the project, together with duration, resources required, inputs, outputs and dependencies. The project plan is a dynamic document — at the end of each phase a review of progress and achievements is necessary and an update is recommended.
- **Initial Assessment of Tools and Techniques** — An initial assessment of tools and techniques to be used. It is important to assess tools and techniques early in the process since the selection possibly influences the entire project.

---

### 2. Data Understanding

The data understanding phase starts with an initial data collection and proceeds with activities in order to get familiar with the data, to identify data quality problems, to discover first insights into the data, or to detect interesting subsets to form hypotheses for hidden information.

#### 2.1 Collect Initial Data

**Task:** Acquire within the project the data (or access to the data) listed in the project resources. This initial collection includes data loading if necessary for data understanding. If you acquire multiple data sources, integration is an additional issue, either here or in data preparation later.

**Output:**

- **Initial Data Collection Report** — List the data set(s) acquired, together with their locations within the project, the methods used to acquire them and any problems encountered.

#### 2.2 Describe Data

**Task:** Examine the "gross" or "surface" properties of the acquired data and report on the results.

**Output:**

- **Data Description Report** — Describe the data which has been acquired, including: the format of the data, the quantity of data (e.g., number of records and fields in each table), the identities of the fields, and any other surface features discovered.

#### 2.3 Explore Data

**Task:** This task tackles the data mining questions which can be addressed using querying, visualisation and reporting. These include: distribution of key attributes, relations between pairs or small numbers of attributes, results of simple aggregations, properties of significant sub-populations, and simple statistical analyses.

**Output:**

- **Data Exploration Report** — Describes results of this task including first findings or initial hypotheses and their impact on the remainder of the project. May include graphs and plots which indicate data characteristics or lead to interesting data subsets for further examination.

#### 2.4 Verify Data Quality

**Task:** Examine the quality of the data, addressing questions such as: Is the data complete? Is it correct or does it contain errors? Are there missing values? If so, how are they represented, where do they occur, and how common are they?

**Output:**

- **Data Quality Report** — List the results of the data quality verification; if quality problems exist, list possible solutions.

---

### 3. Data Preparation

The data preparation phase covers all activities to construct the final dataset (data that will be fed into the modeling tool(s)) from the initial raw data. Data preparation tasks are likely to be performed multiple times, and not in any prescribed order. Tasks include table, record, and attribute selection as well as transformation and cleaning of data for modeling tools.

**Phase-Level Outputs:**

- **Data Set** — The data set(s) produced by the data preparation phase, which will be used for modeling or the major analysis work of the project.
- **Data Set Description** — Describe the dataset(s) which will be used for the modeling or the major analysis work of the project.

#### 3.1 Select Data

**Task:** Decide on the data to be used for analysis. Criteria include relevance to the data mining goals, quality, and technical constraints such as limits on data volume or data types. Note that data selection covers selection of attributes (columns) as well as selection of records (rows) in a table.

**Output:**

- **Rationale for Inclusion / Exclusion** — List the data to be included/excluded and the reasons for these decisions.

#### 3.2 Clean Data

**Task:** Raise the data quality to the level required by the selected analysis techniques. This may involve selection of clean subsets of the data, the insertion of suitable defaults, or more ambitious techniques such as the estimation of missing data by modeling.

**Output:**

- **Data Cleaning Report** — Describes what decisions and actions were taken to address the data quality problems reported during the verify data quality task. Transformations of the data for cleaning purposes and the possible impact on the analysis results should be considered.

#### 3.3 Construct Data

**Task:** This task includes constructive data preparation operations such as the production of derived attributes, entire new records, or transformed values for existing attributes.

**Outputs:**

- **Derived Attributes** — New attributes constructed from one or more existing attributes in the same record. Example: area = length × width.
- **Generated Records** — Completely new records. Example: Create records for customers who made no purchase during the past year. There was no reason to have such records in the raw data, but for modeling purposes it might make sense to explicitly represent the fact that certain customers made zero purchases.

#### 3.4 Integrate Data

**Task:** Methods whereby information is combined from multiple tables or records to create new records or values.

**Output:**

- **Merged Data** — Joining together two or more tables that have different information about the same objects. Also covers aggregations, where new values are computed by summarizing information from multiple records and/or tables.

#### 3.5 Format Data

**Task:** Formatting transformations refer to primarily syntactic modifications made to the data that do not change its meaning, but might be required by the modeling tool.

**Output:**

- **Reformatted Data** — Changes to attribute order, record order, or syntactic changes to satisfy modeling tool requirements (e.g., removing commas from text fields, trimming values, randomizing record order for neural networks).

---

### 4. Modeling

In this phase, various modeling techniques are selected and applied, and their parameters are calibrated to optimal values. Typically, there are several techniques for the same data mining problem type. Some techniques have specific requirements on the form of data. Therefore, stepping back to the data preparation phase is often needed.

#### 4.1 Select Modeling Technique

**Task:** Select the actual modeling technique which is to be used. This task refers to the specific modeling technique, e.g., decision tree building with C4.5 or neural network generation with back propagation. If multiple techniques are applied, perform this task for each technique separately.

**Outputs:**

- **Modeling Technique** — The actual modeling technique which is used.
- **Modeling Assumptions** — Many modeling techniques make specific assumptions on the data (e.g., all attributes have uniform distributions, no missing values allowed, class attribute must be symbolic, etc.).

#### 4.2 Generate Test Design

**Task:** Before actually building a model, generate a procedure or mechanism to test the model's quality and validity. For example, in supervised data mining tasks such as classification, it is common to use error rates as quality measures, typically by separating the data set into train and test sets.

**Output:**

- **Test Design** — Describes the intended plan for training, testing, and evaluating the models. A primary component is deciding how to divide the available data set into training data, test data, and validation data sets.

#### 4.3 Build Model

**Task:** Run the modeling tool on the prepared data set to create one or more models.

**Outputs:**

- **Parameter Settings** — Lists the parameters and their chosen values, along with rationale for the choice of parameter settings.
- **Models** — The actual models produced by the modeling tool, not a report.
- **Model Description** — Describe the resultant model. Report on the interpretation of the models and any difficulties encountered with their meanings.

#### 4.4 Assess Model

**Task:** The data mining engineer interprets the models according to domain knowledge, data mining success criteria, and the desired test design. The engineer tries to rank the results and assesses the models according to the evaluation criteria, also taking into account business objectives and business success criteria as far as possible.

**Outputs:**

- **Model Assessment** — Summarizes results of this task, lists qualities of generated models (e.g., in terms of accuracy), and ranks their quality in relation to each other.
- **Revised Parameter Settings** — According to the model assessment, revise parameter settings and tune them for the next run. Iterate model building and assessment until you strongly believe you found the best model(s).

---

### 5. Evaluation

At this stage in the project you have built a model (or models) that appears to have high quality from a data analysis perspective. Before proceeding to final deployment, it is important to more thoroughly evaluate the model and review the steps executed to construct the model, to be certain it properly achieves the business objectives.

> **Key equation:** RESULTS = MODELS + FINDINGS
>
> The total output of a Data Mining project is not just the models but also findings — anything (apart from the model) that is important in meeting objectives of the business or important in leading to new questions, lines of approach, or side effects.

#### 5.1 Evaluate Results

**Task:** This step assesses the degree to which the model meets the business objectives and seeks to determine if there is some business reason why this model is deficient. Another option is to test the model(s) on test applications in the real application if time and budget constraints permit. Evaluation also assesses other data mining results generated, including findings not necessarily related to the original business objectives.

**Outputs:**

- **Assessment of Data Mining Results w.r.t. Business Success Criteria** — Summarizes assessment results in terms of business success criteria including a final statement whether the project already meets the initial business objectives.
- **Approved Models** — After model assessment w.r.t. business success criteria, the generated models that meet the selected criteria.

#### 5.2 Review Process

**Task:** Do a more thorough review of the data mining engagement to determine if there is any important factor or task that has somehow been overlooked. This review also covers quality assurance issues (e.g., Did we correctly build the model? Did we only use attributes that we are allowed to use and that are available for future analyses?).

**Output:**

- **Review of Process** — Summarizes the process review and gives hints for activities that have been missed and/or should be repeated.

#### 5.3 Determine Next Steps

**Task:** According to the assessment results and the process review, decide whether to finish the project and move on to deployment, initiate further iterations, or set up new data mining projects. This includes analysis of remaining resources and budget.

**Outputs:**

- **List of Possible Actions** — A list of possible further actions along with the reasons for and against each option.
- **Decision** — Describes the decision as to how to proceed along with the rationale.

---

### 6. Deployment

Creation of the model is generally not the end of the project. Even if the purpose of the model is to increase knowledge of the data, the knowledge gained will need to be organized and presented in a way that the customer can use it. Depending on the requirements, the deployment phase can be as simple as generating a report or as complex as implementing a repeatable data mining process.

#### 6.1 Plan Deployment

**Task:** Take the evaluation results and conclude a strategy for deployment. If a general procedure to create the relevant model(s) has been identified, document it here for later deployment.

**Output:**

- **Deployment Plan** — Summarizes deployment strategy including necessary steps and how to perform them.

#### 6.2 Plan Monitoring and Maintenance

**Task:** Monitoring and maintenance are important issues if the data mining result becomes part of the day-to-day business. A careful preparation of a maintenance strategy helps avoid unnecessarily long periods of incorrect usage of data mining results.

**Output:**

- **Monitoring and Maintenance Plan** — Summarizes monitoring and maintenance strategy including necessary steps and how to perform them.

#### 6.3 Produce Final Report

**Task:** At the end of the project, the project leader and team write up a final report. Depending on the deployment plan, this may be a summary of the project and its experiences, or a final presentation of the data mining result(s).

**Outputs:**

- **Final Report** — The final written report of the data mining engagement. Includes all of the previous deliverables, plus summarizing and organizing the results.
- **Final Presentation** — There will also often be a meeting at the conclusion of the project where the results are verbally presented to the customer.

#### 6.4 Review Project

**Task:** Assess what went right and what went wrong, what was done well and what needs to be improved.

**Output:**

- **Experience Documentation** — Summarizes important experiences made during the project (e.g., pitfalls, misleading approaches, hints for selecting the best suited data mining techniques in similar situations). Ideally covers any reports written by individual project members during the project phases.

---

## Part III: The CRISP-DM User Guide

### 1. Business Understanding

#### 1.1 Determine Business Objectives

##### Output: Background

Details about the information known about the organization's business situation at the start of the project. These details serve to more closely identify the business goals and to identify resources that may be used or needed during the course of the project.

**Activities — Organization:**

- Develop organization chart identifying divisions, departments, and project groups (including managers' names and responsibilities)
- Identify key persons in the business and their roles
- Identify an internal sponsor (financial sponsor and primary user/domain expert)
- Identify if there is a steering committee and its members
- Identify the business units impacted by the data mining project (e.g., Marketing, Sales, Finance)

**Activities — Problem Area:**

- Identify the problem area (e.g., Marketing, Customer Care, Business Development)
- Describe the problem in general terms
- Check the current status of the project (e.g., Is it already clear within the business unit that a data mining project is being performed?)
- Clarify prerequisites of the project (e.g., What is the motivation? Does the business already use data mining?)
- If necessary, prepare presentations and present data mining to the business
- Identify target groups for the project result
- Identify the users' needs and expectations

**Activities — Current Solution:**

- Describe the solution currently in use for the problem
- Describe the advantages and disadvantages of the current solution, and the level to which it is accepted by the users

##### Output: Business Objectives

Describe the customer's primary objective, from a business perspective, in the data mining project.

**Activities:**

- Informally describe the problem to be solved with data mining
- Specify all business questions as precisely as possible
- Specify any other business requirements (e.g., The business does not want to lose any customers)
- Specify expected benefits in business terms

> ⚠️ **Beware!** Beware of setting unattainable goals — make them as realistic as possible.

##### Output: Business Success Criteria

Describe the criteria for a successful or useful outcome to the project from the business point of view.

**Activities:**

- Specify business success criteria (e.g., improve response rate in a mailing campaign by 10%, sign-up rate increased by 20%)
- Identify who will assess the success criteria

> ✅ **Remember!** Each of the success criteria should relate to at least one of the specified Business Objectives.

> 💡 **Good Idea!** Before starting with Situation Assessment, consider previous experiences of this problem — either internally using CRISP-DM or externally using pre-packaged solutions.

#### 1.2 Assess Situation

##### Output: Inventory of Resources

List the resources available to the project.

**Activities — Hardware Resources:**

- Identify the base hardware
- Establish the availability of the base hardware for the data mining project
- Check if the hardware maintenance schedule conflicts with availability
- Identify the hardware available for the data mining tool (if the tool is known)

**Activities — Sources of Data & Knowledge:**

- Identify data sources and their types (on-line sources, experts, written documentation, …)
- Identify knowledge sources and their types
- Check available tools and techniques
- Describe the relevant background knowledge (informally or formally)

**Activities — Personnel Sources:**

- Identify project sponsor (if different from internal sponsor)
- Identify system administrator, database administrator and technical support staff
- Identify market analysts, data mining experts and statisticians and check their availability
- Check availability of domain experts for later phases

> ✅ **Remember!** The project may need technical staff at odd times throughout the project (e.g., during Data Transformation).

##### Output: Requirements, Assumptions and Constraints

**Activities — Requirements:**

- Specify target group profile
- Capture all requirements on scheduling
- Capture requirements on comprehensibility, accuracy, deployability, maintainability and repeatability
- Capture requirements on security, legal restrictions, privacy, reporting and project schedule

**Activities — Assumptions:**

- Clarify all assumptions (including implicit ones) and make them explicit
- List assumptions on data quality (e.g., accuracy, availability)
- List assumptions on external factors (e.g., economic issues, competitive products, technical advances)
- Clarify assumptions that lead to any of the estimates
- List all assumptions on whether it is necessary to understand and describe or explain the model

**Activities — Constraints:**

- Check general constraints (e.g., legal issues, budget, timescales and resources)
- Check access rights to data sources (e.g., access restrictions, password required)
- Check technical accessibility of data (operating systems, data management system, file or database format)
- Check whether relevant knowledge is accessible
- Check budget constraints (fixed costs, implementation costs, etc.)

> ✅ **Remember!** The list of assumptions also includes assumptions at the beginning of the project — what has been the starting point of the project.

##### Output: Risks and Contingencies

**Activities — Identify Risks:**

- Identify business risks (e.g., competitor comes up with better results first)
- Identify organisational risks (e.g., department requesting project not having funding)
- Identify financial risks (e.g., further funding depends on initial data mining results)
- Identify technical risks
- Identify risks that depend on data and data sources (e.g., poor quality and coverage)

**Activities — Develop Contingency Plans:**

- Determine conditions when each risk may occur
- Develop contingency plans

##### Output: Terminology

Make a glossary of terminology relevant to the project with two components: (1) a glossary of relevant business terminology, and (2) a glossary of data mining terminology illustrated with examples relevant to the business problem.

**Activities:**

- Check prior availability of glossaries, otherwise begin to draft glossaries
- Talk to domain experts to understand their terminology
- Become familiar with the business terminology

##### Output: Costs and Benefits

Prepare a cost-benefit analysis for the project.

**Activities:**

- Estimate costs for data collection
- Estimate costs of developing and implementing a solution
- Identify benefits when a solution is deployed (e.g., improved customer satisfaction, ROI and increase in revenue)
- Estimate operating costs

> ⚠️ **Beware!** Remember to identify hidden costs such as repeated data extraction and preparation, changes in work flows, and training time during learning.

#### 1.3 Determine Data Mining Goals

##### Output: Data Mining Goals

Describe the intended outputs of the project that will enable the achievement of the business objectives.

**Activities:**

- Translate the business questions to data mining goals (e.g., a marketing campaign requires segmentation of customers; specify the level/size of the segments)
- Specify data mining problem type (e.g., classification, description, prediction and clustering)

> 💡 **Good Idea!** It may be wise to re-define the problem. E.g., modeling product retention rather than customer retention since targeting customer retention may be too late to affect the outcome.

##### Output: Data Mining Success Criteria

Define the criteria for a successful outcome to the project in technical terms.

**Activities:**

- Specify criteria for model assessment (e.g., model accuracy, performance and complexity)
- Define benchmarks for evaluation criteria
- Specify criteria which address subjective assessment criteria (e.g., model explainability and data/marketing insight provided by the model)

> ⚠️ **Beware!** Remember that the Data Mining Success Criteria will be different from the Business Success Criteria defined earlier. Remember that it is wise to plan for deployment already at the start of the project.

#### 1.4 Produce Project Plan

##### Output: Project Plan

List the stages to be executed in the project, together with duration, resources required, inputs, outputs and dependencies.

**Activities:**

- Define the initial process plan and discuss feasibility with all involved personnel
- Put all identified goals and selected techniques together into a coherent procedure
- Estimate effort and resources needed to achieve and deploy the solution (It is often postulated that 50%–70% of time/effort is used in Data Preparation, 20%–30% in Data Understanding, 10%–20% in each of Modeling, Evaluation and Business Understanding, and 5%–10% in Deployment)
- Identify critical steps
- Mark decision points
- Mark review points
- Identify major iterations

##### Output: Initial Assessment of Tools and Techniques

**Activities:**

- Create a list of selection criteria for tools and techniques (or use existing)
- Choose potential tools and techniques
- Evaluate appropriateness of techniques
- Review and prioritise applicable techniques according to the evaluation of alternative solutions

---

### 2. Data Understanding

#### 2.1 Collect Initial Data

##### Output: Initial Data Collection Report

List all the data that will be used within the project, together with any selection requirements.

**Activities — Data Requirements Planning:**

- Plan which information is needed (e.g., only given attributes, additional information)
- Check if all the information needed is actually available

**Activities — Selection Criteria:**

- Specify selection criteria (e.g., Which attributes are necessary? Which are irrelevant? How many attributes can the chosen techniques handle?)
- Select tables/files of interest
- Select data within a table/file
- Consider how much history to use even if more is available

> ⚠️ **Beware!** Data collected from different sources may give rise to quality problems when merged.

**Activities — Insertion of Data:**

- If the data contains free text entries, decide whether to encode them for modelling or group specific entries
- How can missing attributes be acquired?
- Describe how to extract the data

> 💡 **Good Idea!** Some knowledge about the data may be on non-electronic sources. It may be necessary to pre-process the data (time series data, weighted averages, etc.).

#### 2.2 Describe Data

##### Output: Data Description Report

**Activities — Volumetric Analysis of Data:**

- Identify data and method of capture
- Access data sources
- Utilise statistical analyses if appropriate
- Report tables and their relations
- Check data volume, number of tuples, complexity
- Does the data contain free text entries?

**Activities — Attribute Types & Values:**

- Check accessibility and availability of attributes
- Check attribute types (numeric, symbolic, taxonomy, etc.)
- Check attribute value ranges
- Analyse attribute correlations
- Understand the meaning of each attribute and attribute value in business terms
- Compute basic statistics (distributions, averages, max, min, standard deviations, variances, modes, skewness, etc.)
- Analyse basic statistics and relate the results to their meaning in business terms
- Assess attribute relevance for the specific data mining goal
- Check if attribute meaning is used consistently
- Interview domain expert on attribute relevance
- Consider if balancing the data is necessary

**Activities — Keys:**

- Analyse key relations
- Check amount of overlaps of key attribute values across tables

**Activities — Review Assumptions/Goals:**

- Update list of assumptions if necessary

#### 2.3 Explore Data

##### Output: Data Exploration Report

**Activities — Data Exploration:**

- Analyse properties of interesting attributes in detail (e.g., basic statistics, interesting sub-populations)
- Identify characteristics of sub-populations

**Activities — Form Suppositions for Future Analysis:**

- Consider and evaluate information and findings in the Data Descriptions Report
- Form hypotheses and identify actions
- Transform hypotheses into a data mining goal if possible
- Clarify data mining goals or make them more precise (a more directed search towards business objectives is preferable to blind search)
- Perform basic analysis to verify the hypothesis

#### 2.4 Verify Data Quality

##### Output: Data Quality Report

**Activities:**

- Identify special values and catalogue their meaning

**Activities — Review Keys, Attributes:**

- Check coverage (e.g., are all possible values represented)
- Check keys
- Do the meanings of attributes and contained values fit together?
- Identify missing attributes and blank fields
- Check for attributes with different values that have similar meanings (e.g., "low fat" vs. "diet")
- Check spelling of values (e.g., same value with different cases)
- Check for deviations — decide whether a deviation is noise or an interesting phenomenon
- Check for plausibility of values (e.g., all fields have the same or nearly the same values)

> 💡 **Good Idea!** Review any attributes that may give answers conflicting with common sense (e.g., teenagers with high income). Use visualisation plots, histograms, etc. to show inconsistencies in the data.

**Activities — Data Quality in Flat Files:**

- Check which delimiter is used and if it is used consistently
- Check number of fields in each record — do they coincide?

**Activities — Noise and Inconsistencies Between Sources:**

- Check consistencies and redundancies between different sources
- Plan how to deal with noise
- Detect type of noise and which attributes are affected

> 💡 **Good Idea!** It may be necessary to exclude some data that do not exhibit either positive or negative behaviour. Review all assumptions whether they are valid given the current information on data and knowledge.

---

### 3. Data Preparation

#### 3.1 Select Data

##### Output: Rationale for Inclusion / Exclusion

**Activities:**

- Collect appropriate additional data (from different sources — in-house as well as externally)
- Perform significance and correlation test to decide if fields should be included
- Reconsider Data Selection Criteria in light of experiences of data quality, data exploration (may wish to include/exclude other sets of data)
- Reconsider Data Selection Criteria in light of experience of modelling (model assessment may show that other data sets are needed)
- Select different data subsets (e.g., different attributes, only data which meet certain conditions)
- Consider use of sampling techniques (e.g., reduction of test data set size, splitting test and training data sets, weighted samples)
- Document the rationale for inclusion/exclusion
- Check available techniques for sampling data

> 💡 **Good Idea!** Decide if one or more attributes are more important than others and weight the attributes accordingly.

#### 3.2 Clean Data

##### Output: Data Cleaning Report

**Activities:**

- Reconsider how to deal with observed types of noise
- Correct, remove or ignore noise
- Decide how to deal with special values and their meaning (e.g., '99' for unknown data, '00' for 100-year-old people)
- Reconsider Data Selection Criteria in light of experiences of data cleaning

> 💡 **Good Idea!** Some fields may be irrelevant to the data mining goals and therefore noise in those fields has no significance. However, if noise is ignored for these reasons, it should be fully documented as circumstances may change later.

#### 3.3 Construct Data

**Activities:**

- Check available construction mechanisms with the list of tools suggested for the project
- Decide whether it is best to perform the construction inside the tool or outside
- Reconsider Data Selection Criteria in light of experiences of data construction

##### Output: Derived Attributes

New attributes constructed from one or more existing attributes in the same record. Derived attributes might be constructed because: background knowledge convinces us that some fact is important; the modelling algorithm handles only certain types of data; or the outcome of the modelling phase may suggest that certain facts are not being covered.

**Activities — Derived Attributes:**

- Decide if any attribute should be normalized (e.g., when using a clustering algorithm with age and income, the income will dominate)
- Consider adding new information on the relevant importance of attributes (e.g., attribute weights, weighted normalization)
- How can missing attributes be constructed? (decide type of construction: aggregate, average, induction)
- Add new attributes to the accessed data

> 💡 **Good Idea!** Before adding Derived Attributes, try to determine if and how they will ease the model process or facilitate the modelling algorithm. Do not derive attributes simply to reduce the number of input attributes.

**Activities — Single-Attribute Transformations:**

- Specify necessary transformation steps in terms of available transformation facilities
- Perform transformation steps

> 💡 **Hint!** Transformations may be necessary to transform ranges to symbolic fields (e.g., ages to age ranges) or symbolic fields to numeric values. They are often required by the modelling tools or algorithm.

##### Output: Generated Records

Completely new records which add new knowledge or represent data not otherwise represented.

**Activities:**

- Check for available techniques if needed (e.g., mechanisms to construct prototypes for each segment of segmented data)

#### 3.4 Integrate Data

##### Output: Merged Data

Merging tables and generating aggregate values.

**Activities:**

- Check integration facilities if they are able to integrate the input sources as required
- Integrate sources and store result
- Reconsider Data Selection Criteria in light of experiences of data integration

> 💡 **Good Idea!** Remember that some knowledge may be contained in non-electronic format.

#### 3.5 Format Data

##### Output: Reformatted Data

**Activities — Rearranging Attributes:**

- Address tool requirements on the order of the attributes

**Activities — Reordering Records:**

- Change the order of the records in the data set if required by the modeling tool

**Activities — Reformatted Within-Value:**

- Make purely syntactic changes to satisfy the requirements of the specific modeling tool
- Reconsider Data Selection Criteria in light of experiences of data formatting

---

### 4. Modeling

#### 4.1 Select Modeling Technique

**Activities:**

- Decide on appropriate technique for exercise bearing in mind the tool selected

##### Output: Modeling Assumptions

**Activities:**

- Define any built-in assumptions made by the technique about the data (e.g., quality, format, distribution)
- Compare these assumptions with those in the Data Description Report
- Make sure that these assumptions hold and step back to Data Preparation Phase if necessary

#### 4.2 Generate Test Design

##### Output: Test Design

**Activities:**

- Check existing test designs for each data mining goal separately
- Decide on necessary steps (number of iterations, number of folds, etc.)
- Prepare data required for test

#### 4.3 Build Model

##### Output: Parameter Settings

**Activities:**

- Set initial parameters
- Document reasons for choosing those values

##### Output: Models

**Activities:**

- Run the selected technique on the input data set to produce the model
- Post-process data mining results (e.g., editing rules, display trees)

##### Output: Model Description

**Activities:**

- Describe any characteristics of the current model that may be useful for the future

#### 4.4 Assess Model

##### Output: Model Assessment

**Activities:**

- Evaluate result w.r.t. evaluation criteria
- Test result according to a test strategy (e.g., Train & Test, Cross-validation, bootstrapping)
- Compare evaluation results and interpretation
- Create ranking of results w.r.t. success and evaluation criteria
- Select best models
- Interpret results in business terms (as far as possible at this stage)
- Check plausibility of model
- Check impacts for data mining goal
- Check model against given knowledge base to see if the discovered information is novel and useful
- Check reliability of result
- Analyse potentials for deployment of each result
- If there is a verbal description of the generated model (e.g., via rules), assess the rules: are they logical, feasible, are there too many or too few, do they offend common sense?
- Assess results

> 💡 **Good Idea!** "Lift Tables" and "Gain Tables" can be constructed to determine how well the model is predicting.

##### Output: Revised Parameter Settings

**Activities:**

- Reset parameters to give better model

---

### 5. Evaluation

#### 5.1 Evaluate Results

##### Output: Assessment of Data Mining Results w.r.t. Business Success Criteria

**Activities:**

- Understand the data mining result
- Interpret the results in terms of the application
- Check impacts for data mining goal
- Check the data mining result against the given knowledge base to see if the discovered information is novel and useful
- Evaluate and assess result w.r.t. business success criteria
- Compare evaluation results and interpretation
- Create ranking of results w.r.t. business success criteria
- Check impacts of result for initial application goal

##### Output: Approved Models

After model assessment w.r.t. business success criteria, models that meet the selected criteria.

#### 5.2 Review Process

##### Output: Review of Process

**Activities:**

- Analyse data mining process
- Identify failures
- Identify misleading steps
- Identify possible alternative actions, unexpected paths in the process

#### 5.3 Determine Next Steps

##### Output: List of Possible Actions

**Activities:**

- Analyse potential for deployment of each result
- Estimate potential for improvement of current process
- Check remaining resources to determine if they allow additional process iterations
- Recommend alternative continuations
- Refine process plan

##### Output: Decision

**Activities:**

- Rank the possible actions
- Select one of the possible actions
- Document reasons for the choice

---

### 6. Deployment

#### 6.1 Plan Deployment

##### Output: Deployment Plan

**Activities:**

- Develop and evaluate alternative plans for deployment
- Identify possible problems when deploying the data mining results (pitfalls of the deployment)

#### 6.2 Plan Monitoring and Maintenance

##### Output: Monitoring and Maintenance Plan

**Activities:**

- Check for dynamic aspects (i.e., what things could change in the environment?)
- When should the data mining result or model not be used any more? Identify criteria (validity, threshold of accuracy, new data, change in the application domain, etc.)
- What should happen if the model or result can no longer be used? (Update model, set up new data mining project, etc.)
- Will the business objectives of the use of the model change over time? Fully document the initial problem the model was attempting to solve
- Develop Monitoring and Maintenance Plan

#### 6.3 Produce Final Report

##### Output: Final Report

At the end of the project, a final report where all threads are brought together. Includes identifying results obtained, describing the process, showing costs incurred, defining deviations from the original plan, describing implementation plans, and making recommendations for future work.

**Activities:**

- Identify what reports are needed (slide presentation, management summary, detailed findings, explanation of models, …)
- Analyse how well initial data mining goals have been met
- Identify target groups for report
- Outline structure and contents of report(s)
- Select findings to be included in the reports
- Write a report

##### Output: Final Presentation

**Activities:**

- Decide on target group for final presentation (will they already have received final report?)
- Select which items from final report should be included in final presentation

#### 6.4 Review Project

##### Output: Experience Documentation

**Activities:**

- Interview all significant people involved in the project and ask them about their experiences
- If end users work with the data mining result(s), interview them — are they satisfied? What could have been done better? Do they need additional support?
- Summarise feedback and write the experience documentation
- Analyse the process (things that worked well, mistakes made, lessons learned, …)
- Document the specific data mining process (How can the results and experience be fed back into the process?)
- Abstract from details to make the experience useful for future projects

---

## Part IV: The CRISP-DM Outputs

This part is intended to contain document templates for each output in the CRISP-DM Process Model accompanied by brief descriptions of its main purpose and contents. For outputs other than documents (e.g., models and data sets), this part includes additional hints on how to generate these types of outputs.

> *Note: This part was not completely finished in the original 1999 discussion paper.*

---

## Part V: Appendix

### 1. Glossary / Terminology

| Term | Definition |
|------|-----------|
| **CRISP-DM Methodology** | The general term for all concepts developed and defined in CRISP-DM |
| **Process Model** | Defines the structure of data mining projects and provides guidance for their execution; consists of Reference Model and User Guide |
| **Phase** | High-level term for part of the process model; consists of related tasks |
| **Task** | Part of a phase; series of activities to produce one or more outputs |
| **Generic Task** | A task which holds across all possible data mining projects; as complete and stable as possible |
| **Specialized Task** | A task which makes specific assumptions in specific data mining contexts |
| **Output** | Tangible result of performing a task; decomposed into output components |
| **Output Component** | Part of an output |
| **Activity** | Part of a task in the user guide; describes actions to perform a task |
| **Process Instance** | A specific project described in terms of the process model |
| **Reference Model** | Decomposition of data mining projects into phases, tasks, and outputs |
| **User Guide** | Specific advice on how to perform data mining projects |
| **Frame** | Information structure to record activities and outputs |
| **Template** | Set of frames or set of templates |
| **Data Mining Context** | Set of constraints and assumptions such as problem type, techniques or tools, application domain |
| **Data Mining Problem Type** | Class of typical data mining problems such as data description and summarization, segmentation, concept descriptions, classification, prediction, dependency analysis |
| **Model** | Ability to apply to a data set to predict a target attribute; executable |

### 2. Data Mining Problem Types

Usually, the data mining project involves a sequence of different problem types which together solve the business problem.

#### 2.1 Data Description and Summarisation

Aims at the concise description of characteristics of the data, typically in elementary and aggregated form, giving the user an overview of the structure of the data. Sometimes data description and summarisation alone can be an objective of a data mining project (e.g., a retailer interested in turnover of all outlets broken down by categories).

In almost all data mining projects, data description and summarisation is a subgoal in the process, typically in early stages. Initial exploratory data analysis can help to understand the nature of the data and find potential hypotheses for hidden information.

Data description and summarisation typically occurs in combination with other data mining problem types and is advisable to carry out before any other problem type is addressed. Many reporting systems, statistical packages, OLAP and EIS systems can cover this problem type.

#### 2.2 Segmentation

Aims at the separation of the data into interesting and meaningful subgroups or classes where all members of a subgroup share common characteristics. Segmentation can be performed manually or (semi-)automatically using clustering techniques.

Segmentation can be a data mining problem type of its own, or a step towards solving other problem types (to keep the size of the data manageable or to find homogeneous data subsets which are easier to analyse).

**Appropriate techniques:** Clustering techniques, Neural nets, Visualisation

**Example:** A car company divides its customers into subgroups using cluster analysis based on socio-economic characteristics, then analyses the structure of each subgroup. Specific marketing strategies are deployed for each group separately.

#### 2.3 Concept Descriptions

Aims at an understandable description of concepts or classes. The purpose is not to develop complete models with high prediction accuracy but to gain insights. Concept descriptions need not be complete — it is sufficient if they describe important parts of the concepts or classes.

**Appropriate techniques:** Rule induction methods, Conceptual clustering

**Example:** Using rule induction on car buyer data:
- If SEX = male and AGE > 51 then CUSTOMER = loyal
- If SEX = female and AGE > 21 then CUSTOMER = loyal
- If PROFESSION = manager and AGE < 51 then CUSTOMER = disloyal
- If FAMILY STATUS = bachelor and AGE < 51 then CUSTOMER = disloyal

#### 2.4 Classification

Assumes a set of objects (characterised by attributes/features) belonging to different classes, where the class label is a discrete (symbolic) value known for each object. The objective is to build classification models (classifiers) which assign the correct class label to previously unseen and unlabeled objects.

Classification is one of the most important data mining problem types occurring in a wide range of applications. Many data mining problems can be transformed to classification problems (e.g., credit scoring with classes "good" and "bad" customers).

**Appropriate techniques:** Discriminant analysis, Rule induction methods, Decision tree learning, Neural nets, k Nearest Neighbour, Case-based reasoning, Genetic algorithms

**Example:** Banks develop systems to classify new customers as good or bad credit risks, combining financial information with demographic data.

#### 2.5 Prediction

Very similar to classification — the only difference is that the target attribute is not a qualitative discrete attribute but a continuous one. The aim is to find the numerical value of the target attribute for unseen objects. In the literature, this is sometimes called regression. When dealing with time series data, it is often called forecasting.

**Appropriate techniques:** Regression analysis, Regression trees, Neural nets, k Nearest Neighbour, Box-Jenkins methods, Genetic algorithms

**Example:** A company predicts its expected annual revenue using correlations with advertisement, exchange rate, inflation rate, etc.

#### 2.6 Dependency Analysis

Finding a model which describes significant dependencies (or associations) between data items or events. Dependencies can be used for predictive modelling but are mostly used for understanding. Dependencies can be strict or probabilistic.

**Associations** are a special case of dependencies — data items or events which frequently occur together. A typical application is shopping basket analysis.

In large data sets, dependencies are seldom significant because many influences overlay each other. In such cases it is advisable to perform dependency analysis on more homogeneous segments of the data.

**Sequential patterns** are a special kind of dependencies where sequences of events are considered over time.

**Appropriate techniques:** Correlation analysis, Regression analysis, Association rules, Bayesian networks, Inductive Logic Programming, Visualisation techniques

**Example 1:** A business analyst discovers a significant dependency between total sales of a product and its price and advertisement expenditures, enabling control of sales levels.

**Example 2:** A car company finds that when a radio is ordered, an automatic gearbox is ordered as well in 95% of all cases, leading to offering these accessories as a combination for cost reduction.
