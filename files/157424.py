<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="f2"/>
        <attribute name="authors" value="thasa"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-19 02:45:37 AM"/>
        <attribute name="created" value="dGhhc2E7REVTS1RPUC1DUTY0VDBNOzIwMjUtMDctMTg7MDk6MzU6MTQgUE07Mjg2Ng=="/>
        <attribute name="edited" value="dGhhc2E7REVTS1RPUC1DUTY0VDBNOzIwMjUtMDctMTk7MDI6NDU6MzcgQU07ODsyOTY2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="x, y" type="Integer" array="False" size=""/>
            <output expression="&quot; Input start number: &quot;" newline="True"/>
            <input variable="x"/>
            <output expression="&quot; Input end number : &quot;" newline="True"/>
            <input variable="y"/>
            <while expression="x&lt;y">
                <output expression="x" newline="True"/>
                <assign variable="x" expression="x + 1"/>
            </while>
            <output expression="x" newline="True"/>
        </body>
    </function>
</flowgorithm>