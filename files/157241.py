<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="dolabflow3"/>
        <attribute name="authors" value="itpud"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 09:37:48 PM"/>
        <attribute name="created" value="aXRwdWQ7TEFQVE9QLU05MlRCM0Q5OzI1NjgtMDctMTY7MDk6MDc6MzIgUE07Mjg2OQ=="/>
        <attribute name="edited" value="aXRwdWQ7TEFQVE9QLU05MlRCM0Q5OzI1NjgtMDctMTY7MDk6Mzc6NDggUE07MTsyOTg3"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="number, startnumber, endnumber" type="Integer" array="False" size=""/>
            <declare name="i, n" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="startnumber"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="endnumber"/>
            <while expression="startnumber &lt;= endnumber">
                <output expression="startnumber" newline="True"/>
                <assign variable="startnumber" expression="startnumber+1"/>
            </while>
        </body>
    </function>
</flowgorithm>