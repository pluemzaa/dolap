<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Flow&#3586;&#3657;&#3629;3"/>
        <attribute name="authors" value="nitip"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 05:35:24 PM"/>
        <attribute name="created" value="bml0aXA7TVNJOzI1NjgtMDctMjI7MDU6MzE6NTggUE07MjA3OQ=="/>
        <attribute name="edited" value="bml0aXA7TVNJOzI1NjgtMDctMjI7MDU6MzU6MjQgUE07MTsyMTg0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="numStart" type="Integer" array="False" size=""/>
            <declare name="numEnd" type="Integer" array="False" size=""/>
            <output expression="&quot; Input start number: &quot;" newline="True"/>
            <input variable="numStart"/>
            <output expression="&quot; Input end number: &quot;" newline="True"/>
            <input variable="numEnd"/>
            <while expression="numStart &lt;= numEnd">
                <output expression="numStart" newline="True"/>
                <assign variable="numStart" expression="numStart + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>