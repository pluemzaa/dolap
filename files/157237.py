<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4_4"/>
        <attribute name="authors" value="Pakamas Mungpao"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 09:00:34 PM"/>
        <attribute name="created" value="UGFrYW1hcyBNdW5ncGFvO0RFU0tUT1AtRFVJUkdGUDsyNTY4LTA3LTE2OzA4OjA2OjI0IFBNOzM4NzI="/>
        <attribute name="edited" value="UGFrYW1hcyBNdW5ncGFvO0RFU0tUT1AtRFVJUkdGUDsyNTY4LTA3LTE2OzA4OjE2OjU3IFBNOzE7Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6NDI6MDAgUE07dGVzdDRfTGFiNC5mcHJnOzgwNzI="/>
        <attribute name="edited" value="UGFrYW1hcyBNdW5ncGFvO0RFU0tUT1AtRFVJUkdGUDsyNTY4LTA3LTE2OzA5OjAwOjM0IFBNOzI7Mzk3Nw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="i, years" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <assign variable="interest" expression="interest / 100"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i &lt; years">
                <assign variable="money" expression="money * (1 + interest)"/>
                <output expression="&quot;Year &quot; &amp; (i+1) &amp; &quot;: &quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>