<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_04"/>
        <attribute name="authors" value="Staff"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 02:28:30 PM"/>
        <attribute name="created" value="U3RhZmY7REVTS1RPUC1IUEtPSzhSOzI1NjgtMDctMjA7MDE6MTc6NTEgUE07Mjg5MQ=="/>
        <attribute name="edited" value="U3RhZmY7REVTS1RPUC1IUEtPSzhSOzI1NjgtMDctMjA7MDI6Mjg6MzAgUE07MjszMDAw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="interest, years, totalyears" type="Integer" array="False" size=""/>
            <assign variable="years" expression="1"/>
            <declare name="afterInterest, money, money1, monye2, money3, amount" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="totalyears"/>
            <while expression="years &lt;= totalyears">
                <assign variable="money" expression="money + (money * (interest/100))"/>
                <output expression="&quot;Year&quot; &amp; years &amp; &quot;:&quot; &amp; money" newline="True"/>
                <assign variable="years" expression="years + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>