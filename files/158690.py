<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Flow&#3586;&#3657;&#3629;4"/>
        <attribute name="authors" value="nitip"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 05:48:35 PM"/>
        <attribute name="created" value="bml0aXA7TVNJOzI1NjgtMDctMjI7MDU6Mzk6NTcgUE07MjA4Ng=="/>
        <attribute name="edited" value="bml0aXA7TVNJOzI1NjgtMDctMjI7MDU6NDg6MzUgUE07MTsyMTkw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="interest, years, totalYears" type="Integer" array="False" size=""/>
            <assign variable="years" expression="1"/>
            <declare name="afterInterest, money, money1, money2, money3, amount" type="Real" array="False" size=""/>
            <output expression="&quot; Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <assign variable="amount" expression="money"/>
            <output expression="&quot; Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot; Input years: &quot;" newline="True"/>
            <input variable="totalYears"/>
            <while expression="years &lt;= totalYears">
                <assign variable="amount" expression="amount + (amount * (Interest/100))"/>
                <output expression="&quot; Year &quot; &amp; years &amp; &quot;: &quot; &amp; amount" newline="True"/>
                <assign variable="years" expression="years + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>