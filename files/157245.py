<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="dolabflow4"/>
        <attribute name="authors" value="itpud"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 11:09:41 PM"/>
        <attribute name="created" value="aXRwdWQ7TEFQVE9QLU05MlRCM0Q5OzI1NjgtMDctMTY7MDk6Mzg6MzcgUE07Mjg3OA=="/>
        <attribute name="edited" value="aXRwdWQ7TEFQVE9QLU05MlRCM0Q5OzI1NjgtMDctMTY7MTE6MDk6NDEgUE07NTsyOTc2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, year, i" type="Integer" array="False" size=""/>
            <declare name="year1, year2, year3" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i &lt; year">
                <output expression="&quot; Year &quot; &amp; (i+1) &amp; &quot;: &quot;  &amp; money*(1+(interest/100))" newline="True"/>
                <assign variable="money" expression="money*(1+(interest/100))"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>