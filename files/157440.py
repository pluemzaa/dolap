<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab_403"/>
        <attribute name="authors" value="Staff"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 11:22:58 AM"/>
        <attribute name="created" value="U3RhZmY7REVTS1RPUC1IUEtPSzhSOzI1NjgtMDctMTk7MTE6MTU6MjcgQU07Mjg4Ng=="/>
        <attribute name="edited" value="U3RhZmY7REVTS1RPUC1IUEtPSzhSOzI1NjgtMDctMTk7MTE6MjI6NTggQU07MTsyOTk2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="numstart, numend" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="numstart"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="numend"/>
            <while expression="numstart &lt;= numend">
                <output expression="numstart" newline="True"/>
                <assign variable="numstart" expression="numstart + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>