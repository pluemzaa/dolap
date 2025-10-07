<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="counter_683380337_0.fprg2"/>
        <attribute name="authors" value="HP"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 12:03:41 PM"/>
        <attribute name="created" value="SFA7TEFQVE9QLUxWTUZVM0RROzI1NjgtMDctMjI7MTE6MjU6MTIgQU07MjUyOA=="/>
        <attribute name="edited" value="SFA7TEFQVE9QLUxWTUZVM0RROzI1NjgtMDctMjI7MTI6MDM6NDEgUE07NDsyNjUz"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, total, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="total" expression="money"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; years">
                <assign variable="i" expression="i+1"/>
                <assign variable="total" expression="total * (1 + interest/100)"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot; &amp; total" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>